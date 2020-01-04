provider "aws" {
  access_key = "${var.aws_access_key}"
  secret_key = "${var.aws_secret_key}"
  region = "${var.aws_region}"
}
resource "aws_vpc" "vpc_id" {
  cidr_block = "10.0.0.0/16"
    tags = {
    Name = "vpc-TF"
  }
}
resource "aws_subnet" "public_subnet1_TF" {
  vpc_id = "${aws_vpc.vpc_id.id}"
  cidr_block = "10.0.0.0/24"
  map_public_ip_on_launch = "true"
  availability_zone = "ap-south-1a"
    tags = {
    Name = "public_subnet1_TF"
  }
}

resource "aws_subnet" "public_subnet2_TF" {
  vpc_id = "${aws_vpc.vpc_id.id}"
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = "true"
  availability_zone = "ap-south-1b"
    tags = {
    Name = "public_subnet2_TF"
  }
}

resource "aws_subnet" "Private_subnet1_TF" {
  vpc_id = "${aws_vpc.vpc_id.id}"
  cidr_block = "10.0.2.0/24"
  map_public_ip_on_launch = "false"
  availability_zone = "ap-south-1a"
    tags = {
    Name = "private_subnet1_TF"
  }
}

resource "aws_subnet" "Private_subnet2_TF" {
  vpc_id = "${aws_vpc.vpc_id.id}"
  cidr_block = "10.0.3.0/24"
  map_public_ip_on_launch = "false"
  availability_zone = "ap-south-1b"
    tags = {
    Name = "private_subnet1_TF"
  }
}
resource "aws_security_group" "vpc_sg_TF" {
  name = "vpc_sg"
  vpc_id = "${aws_vpc.vpc_id.id}"
  ingress {
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_blocks = ["114.79.180.62/32"]
  }
  ingress {
      from_port   = 5432
      to_port     = 5432
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    protocol = "tcp"
    from_port = "0"
    to_port = "65535"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "vpc_SG_TF"
  }

}

resource "aws_internet_gateway" "gateway_TF" {
  vpc_id = "${aws_vpc.vpc_id.id}"
    tags = {
    Name = "gateway_TF"
  }
}

resource "aws_default_route_table" "route_table_TF" {
    default_route_table_id = "${aws_vpc.vpc_id.default_route_table_id}"
    route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.gateway_TF.id}"
  }
    tags = {
      Name = "main_TF"
  }
}

resource "aws_route_table_association" "public_subnet_1" {
  subnet_id      = "${aws_subnet.public_subnet1_TF.id}"
  route_table_id = "${aws_default_route_table.route_table_TF.id}"
}

resource "aws_route_table_association" "public_subnet_2" {
  subnet_id      = "${aws_subnet.public_subnet2_TF.id}"
  route_table_id = "${aws_default_route_table.route_table_TF.id}"
}


resource "aws_elb" "load-balancer-TF" {
  name               = "load-balancer-TF"
  connection_draining  = true
  listener {
    instance_port     = 80
    instance_protocol = "HTTP"
    lb_port           = 80
    lb_protocol       = "HTTP"
  }
  health_check {
    healthy_threshold   = 4
    unhealthy_threshold = 2
    timeout             = 5
    target              = "HTTP:80/"
    interval            = 30
  }
  security_groups = ["${aws_security_group.vpc_sg_TF.id}"]
  subnets = [
    "${aws_subnet.public_subnet1_TF.id}",
    "${aws_subnet.public_subnet2_TF.id}",
  ]
  tags = {
    Name = "load_balencer_TF"
  }
}

data "aws_iam_role" "iam_role_TF" {
  name = "CodeDeployDemo-EC2-Instance-Profile"
}

data "aws_ami" "ami_TF" {
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["416604440517"]
}

resource "aws_launch_configuration" "launch-config_TF" {
  image_id      = "${data.aws_ami.ami_TF.id}"
  instance_type = "t2.micro"
  iam_instance_profile = "${data.aws_iam_role.iam_role_TF.id}"
  security_groups = ["${aws_security_group.vpc_sg_TF.id}"]
  key_name = "amazon1"
}

resource "aws_autoscaling_group" "auto_scaling_TF" {
  name = "auto-scaling-TF"
  launch_configuration = "${aws_launch_configuration.launch-config_TF.id}"
  default_cooldown = "250"
  desired_capacity = "${var.desired_capacity}"
  max_size = "${var.max_capacity}"
  min_size = "${var.min_capacity}"
  load_balancers = ["${aws_elb.load-balancer-TF.name}"]
  availability_zones = ["ap-south-1a","ap-south-1b","ap-south-1c"]
  vpc_zone_identifier = [
    "${aws_subnet.public_subnet1_TF.id}",
    "${aws_subnet.public_subnet2_TF.id}"
  ]
}


resource "aws_security_group" "db_sg_TF" {
  name = "db_sg"
  vpc_id = "${aws_vpc.vpc_id.id}"
  ingress {
      from_port   = 5432
      to_port     = 5432
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    protocol = "tcp"
    from_port = "0"
    to_port = "65535"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "db_SG_TF"
  }

}
resource "aws_db_subnet_group" "db_subnet_group" {
  subnet_ids = [
    "${aws_subnet.Private_subnet1_TF.id}",
    "${aws_subnet.Private_subnet2_TF.id}"
  ]
  
}

resource "aws_db_instance" "db_instance" {
  allocated_storage    = "${var.db_size}"
  engine               = "postgres"
  engine_version       = "11.5"
  instance_class       = "db.t2.micro"
  name                 = "${var.db_name}"
  username             = "${var.db_usr_name}"
  password             = "${var.db_pass}"
  vpc_security_group_ids = ["${aws_security_group.db_sg_TF.id}"]
  db_subnet_group_name = "${aws_db_subnet_group.db_subnet_group.id}"
  skip_final_snapshot = true
    tags = {
    Name = "chatapp--db-TF"
  }
}

resource "aws_codedeploy_app" "Chatapp_TF" {
  name = "${var.app_name}"
  compute_platform = "Server"
}

resource "aws_codedeploy_deployment_config" "Code_deploy_config_TF" {
  deployment_config_name = "Code_deploy_config_TF"
  minimum_healthy_hosts {
    type  = "HOST_COUNT"
    value = 0
  }
}

resource "aws_codedeploy_deployment_group" "code_dep_Grp_TF" {
  deployment_group_name = "code_dep_Grp_TF"
  app_name = "${aws_codedeploy_app.Chatapp_TF.name}"
  load_balancer_info {
    elb_info {
      name = "${aws_elb.load-balancer-TF.name}"
    }
  }
  service_role_arn = "arn:aws:iam::416604440517:role/CodeDeployServiceRole"
  autoscaling_groups = ["${aws_autoscaling_group.auto_scaling_TF.name}"]
  deployment_config_name = "${aws_codedeploy_deployment_config.Code_deploy_config_TF.id}"
  deployment_style {
    deployment_option = "WITH_TRAFFIC_CONTROL"
    deployment_type   = "BLUE_GREEN"
  }
}

