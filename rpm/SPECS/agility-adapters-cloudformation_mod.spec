# Header
Name: agility-adapters-kubernetes
Summary: Agility Platform - Kubernetes Service Adapter
Version: %rpm_version
Release: %rpm_revision
Vendor: CSC Agility Dev
URL: http://www.csc.com/
Group: Services/Cloud
License: Commercial
BuildArch: noarch
Requires: jre >= 1.8.0
Requires: agility-platform-common

# Sections
%description
Enables orchestration of container based workloads into Kubernetes cluster.

com.servicemesh.agility.adapters.service.cloudformation
	Copyright (C) 2015-Present Computer Sciences Corporation

Computer Sciences Corporation can be contacted at: info@csc.com


Licensed under the Apache License, Version 2.0 (the "License"); you may not
use or distribute com.servicemesh.agility.adapters.core.aws  except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


To contribute to this project, please see Contributor License Agreement (CLA) and other open source information at:
	https://github.com/csc/csc-open-source



%files
%defattr(644,smadmin,smadmin,755)
/opt/agility-platform/deploy/*
