# https://jdk.java.net/archive/
export JDK8_HOME="${HOME}/opt/java/jdk-8"
export JDK11_HOME="${HOME}/opt/java/jdk-11"
# export JDK13_HOME="${HOME}/opt/java/jdk-13"
export JDK17_HOME="${HOME}/opt/java/jdk-17"
# export JDK21_HOME="${HOME}/opt/java/jdk-21"

switch_java() {
  local version="JDK$1_HOME"

  if [ -z "${!version}" ]; then
    echo "Invalid version."
    return 1
  fi

  export JAVA_HOME="${!version}"
  export PATH=$JAVA_HOME/bin:$PATH
  echo "JAVA_HOME switched to Java $1"
}

# https://maven.apache.org/install.html
export MVN_HOME="${HOME}/opt/apache-maven-3.9.9"
export PATH=$MVN_HOME/bin:$PATH
