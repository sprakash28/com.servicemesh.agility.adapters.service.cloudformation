# com.servicemesh.agility.adapters.service.cloudformation

CSC Agility Platform - Service Adaptor for AWS CloudFormation

This adapter enables access to any AWS service or set of services/infrastructure that can be expressed as a cloud formation template. The cloud formation template is wrapped by the adapter and exposed as an agility blueprint service with inputs/outputs defined by the template. This allows the service to be integrated into more complex blueprints and policy/governance controls placed around their provisioning.

# Usage

CloudFormation templates should be placed in Amazon S3 in a folder accessible via https by the agility platform instance. A service provider instance is configured in admin "network services" under the associated amazon ec2 cloud provider. URLs to the cloud formation templates are configured in the provider configuration dialog. The adapter pulls the templates and builds a blueprint service asset type for each template with attributes corresponding to the template input paramter set.

Node that this adapter requires Agility Platform version 10.2.1 or greater.

# Build

This adapter is dependent on the following:

* Agility Platform Services SDK: The services sdk is open source and can be found on github at https://github.com/csc/csc-agility-platform-sdk. See the included documentation for instructions on building the sdk and its dependencies. The adapter build assumes the services sdk is checked out and built in a relative path of ../agility-platform-sdk
* Agility Platform AWS Library:
* Java 8
* Ant (http://ant.apache.org/) version >= 1.9.3. Must be installed and the ant script located in your path.
* Ivy ((http://ant.apache.org/ivy/) Required for dependency management and should be installed/included in your ant installation.

After satisfying the above dependencies:

<code>ant clean deploy</code>

and pakaged with:

<code>ant clean rpm-build</code>

## License
The CloudFormations adapter is distributed under the Apache 2.0 license. See the [LICENSE](https://github.com/csc/com.servicemesh.agility.adapters.core.aws/blob/master/LICENSE) file for full details.
