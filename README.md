## SUTs

### Feature Service

Github: https://github.com/JavierMF/features-service/tree/develop

Dependencies:

-   OpenJDK 8
-   Maven 3.9.9
-   JaCoCo 0.8.12
-   Spring Boot 1.3.3.RELEASE

Add to `pom.xml`:

```xml
<project>
    <properties>
        <jacoco.version>0.8.12</jacoco.version>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>${spring-boot.version}</version>
                    <configuration>
                        <jvmArguments>
                            -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.build.directory}/jacoco.exec
                        </jvmArguments>
                    </configuration>
            </plugin>

            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <version>${jacoco.version}</version>
                <executions>
                    <execution>
                        <id>integration-test</id>
                        <goals>
                            <goal>prepare-agent</goal>
                        </goals>
                        <phase>integration-test</phase>
                    </execution>

                    <execution>
                    <id>report</id>
                        <goals>
                            <goal>report</goal>
                        </goals>
                        <phase>post-integration-test</phase>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

**Build, Run, Test and Report**

1.   `mvn clean`
2.   `mvn install`
3.   `mvn spring-book:run`
4.   `mvn jacoco:report`

When you add the `jvmArguments` in the `spring-boot-maven-plugin`, you can use the `mvn spring-boot:run` to run the project with a JaCoCo agent. Otherwise, you need to run the project use `java` command:

```shell
java \
-javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.build.directory}/jacoco.exec \
-jar target/features-service-1.0.0-SNAPSHOT.jar
```

**Access**

Access the system throgh `http://localhost:8080` by default, e.g. `http://localhost/products`.

**DB**

Feature Service uses the H2 as database, which is a in-memory, embedded database writen in Java. You can access the db console through `http://localhost:8080/h2-console` with the jdbc `jdbc:h2:mem:testdb`, which is the default property provided by Spring-boot.

**Report**

When you shutdown the system, a `jacoco.exec` file will be generated in `target/` folder. Then, run the `mvn jacoco:report` and will generate the report located in `target/site/jacoco`. Open the `index.html` and you can check the code coverage. JaCoCo will also generate a `jacoco.csv` file in the same folder contain the overview data.



### PetStore (no full code)

Github: https://github.com/swagger-api/swagger-petstore/releases/tag/swagger-petstore-v3-1.0.26

Version: 1.0.26



### ProShop

https://anonymous.4open.science/r/proshop-api-B648 inaccessible from 6, Apr, 2025

Postgresql 12.22

coverage==7.6.1
fastapi==0.115.12
psycopg2-binary==2.9.10
pydantic==2.10.6
pydantic-core==2.27.2
python-dotenv==1.0.1
uvicorn==0.33.0
sqlalchemy=2.0.2
fastapi-sqlalchemy=0.2.1

Python 3.8.10

```shell
pip install -r requirements.txt
coverage run --branch -m uvicorn src.main:app --host=0.0.0.0 --port=8000
coverage report --csv=coverage_report.csv
```

```shell
sudo apt install postgresql postgresql-contrib
sudo -i -u postgres
alter user postgres with password '12345678';
create database proshop;
\l
\q
psql -U postgres -h localhost -d postgres
psql postgres://postgres:12345678@localhost:5432/proshop
```



## Tools

### EvoMaster

Dependencies: Java version 8 or later, Maven

Build & Install: 

```shell
git clone https://github.com/EMResearch/EvoMaster.git
cd EvoMaster
mvn clean install -DskipTests
```

Black-Box Testing Command

```shell
java -jar core/target/evomaster.jar  --blackBox true --bbSwaggerUrl https://api.apis.guru/v2/openapi.yaml  --outputFormat JAVA_JUNIT_4 --maxTime 30s --ratePerMinute 60 --outputFolder ../src_evo/src/test/java
```

- `java -jar core/target/evomaster.jar`，编译完成后的Jar包，位于`EvoMaster/core/target/`下；
- `--blackBox true`，默认是白盒，使用该选项设置为黑盒；
- `--bbSwaggerUrl ...`，OpenApi/Swagger Spec，服务器地址为文档中的`host`或`servers`参数，如果没有则默认为本地，也可以通过`--bbTargetUrl`指定，该选项会覆盖spec中的参数；
- `--outputFormat JAVA_JUNIT_4`，测时生成方式，必须指定，这里在Java中使用JUnit4；
- `-maxTime 30s`，搜索时间，一般可分别搜索`10m`、`1h`、`24h`；
- `--ratePerMinute 60`，避免频繁的调用被检测为DoS攻击，这里每秒钟调用1次；
- `--outputFolder ../src_evo/src/test/java`，测试用例输出目录。

Artifact：==./evomaster-apisguru==

- 生成用例可运行：
  
  - [x] 是
  - [ ] 否
  
- 运行脚本：

  ```shell
  ...
  ```



### Schemathesis



### RESTler



### APIFuzzer



### Dredd



## JDK

https://openjdk.org/install/

**OpenJDK 8**

-   https://adoptium.net/temurin/nightly/?version=8

**OpenJDK 9+**

-   https://jdk.java.net/archive/
-   https://jdk.java.net/\<version\>
