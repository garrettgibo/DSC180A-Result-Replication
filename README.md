# DSC 180A Result Replication

[Assignments Link](https://dsc-capstone.github.io/assignments/quarter-1-methodology/)


## Running the Project

To run any of the following targets, the command is:

```sh
python run.py <target>
```

### robot

`robot` creates an instance of the
[dronekit-sitl](https://dronekit-python.readthedocs.io/en/latest/develop/sitl_setup.html),
which can be used to generate realistic sensor data that can be used
as a template for the following targets.

### robot_client

`robot_client` provides the interface to connect to a specified robot.
The client connects over tcp or udp and uses the
[MAVLink](https://mavlink.io/en/messages/common.html), standard for
the messages.

### clean_gps

`clean_gps` will extract, transform, and clean the raw gps data so
that it can be used for anaylsis.

### report

`report` will have the necessary methods to create a report of the
findings.

### Responsibilities
* Garrett Gibo developed the skeleton structure of the repository.
* Neghena Faizyar developed edits to the readme.md
* Shiyin Liang developed edits to the readme.md


## Docker

```sh
# Build
docker build -t <user>/<image-name> -f Docker/Dockerfile .
# Push
docker push <user>/<image-name>
```
