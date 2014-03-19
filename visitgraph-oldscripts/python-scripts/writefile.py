from random import randint


DEPENDENCIES = [

                "org.springframework:org.springframework.aop:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.aspects:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.asm:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.beans:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.core:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.context:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.context.support:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.expression:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.jdbc:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.jms:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.orm:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.oxm:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.transaction:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.web:jar:3.1.1.RELEASE",
                "org.springframework:org.springframework.web.servlet:jar:3.1.1.RELEASE",
                "org.apache.commons:com.springsource.org.apache.commons.collections:jar:3.2.1",
                "org.apache.commons:com.springsource.org.apache.commons.lang:jar:2.5.0",
                "org.apache.commons:com.springsource.org.apache.commons.pool:jar:1.5.3",
                "org.apache.commons:com.springsource.org.apache.commons.codec:jar:1.4.0",
                "org.apache.commons:com.springsource.org.apache.commons.validator:jar:1.3.1",
                "org.apache.commons:com.springsource.org.apache.commons.fileupload:jar:1.2.1",
                "org.apache.commons:com.springsource.org.apache.commons.beanutils:jar:1.8.0",
                "org.apache.commons:com.springsource.org.apache.commons.io:jar:1.4.0",
                "org.apache.commons:com.springsource.org.apache.commons.dbcp:jar:1.2.2.osgi",
                "org.apache.axis:com.springsource.org.apache.axis:jar:1.4.0",


                "org.apache.hadoop:hadoop-hdfs:jar:2.2.0",
                "org.apache.hadoop:hadoop-auth:jar:2.2.0",
                "org.apache.hadoop:hadoop-common:jar:2.2.0",
                "org.apache.hadoop:hadoop-mapreduce-client-common:jar:2.2.0",
                "org.apache.hadoop:hadoop-mapreduce-client-app:jar:2.2.0",
                "org.apache.hadoop:hadoop-mapreduce-client-jobclient:jar:2.2.0",
                "org.apache.hadoop:hadoop-mapreduce-client-core:jar:2.2.0",
                'commons-configuration:commons-configuration:jar:1.6',
                "org.apache.hadoop:hadoop-annotations:jar:2.2.0",
                'org.apache.hbase:hbase-client:jar:0.96.0-hadoop2',
                'org.apache.hbase:hbase-common:jar:0.96.0-hadoop2',
                'org.apache.hbase:hbase-protocol:jar:0.96.0-hadoop2',
                'org.cloudera.htrace:htrace-core:jar:2.01',
                'io.netty:netty:jar:3.6.6.Final',




                "org.apache.activemq:activemq-core:jar:5.7.0",
                "org.apache.activemq:activemq-all:jar:5.7.0",


                "storm:storm:jar:0.9.0.1",
                'org.apache.commons:commons-exec:jar:1.1',


                "org.joda:com.springsource.org.joda.time:jar:1.6.0",
                "org.joda:joda-convert:jar:1.1",


                "org.codehaus.jackson:jackson-mapper-asl:jar:1.8.5",
                "org.codehaus.jackson:jackson-core-asl:jar:1.8.5",



                "com.google.code.gson:gson:jar:2.1",
                'com.googlecode.json-simple:json-simple:jar:1.1',


                "com.google.protobuf:protobuf-java:jar:2.5.0",


                'redis.clients:jedis:jar:2.1.0',


                "net.sf.jung:jung-algorithms:jar:2.0.1",
                "net.sf.jung:jung-io:jar:2.0.1",
                "net.sf.jung:jung-graph-impl:jar:2.0.1",
                "net.sf.jung:jung-api:jar:2.0.1",



                "org.apache.hadoop:hadoop-core:jar:1.2.1",
                "org.apache.mahout:mahout-math:jar:0.7",
                "org.apache.mahout:mahout-core:jar:0.7",
                "org.apache.mahout:mahout-buildtools:jar:0.7",
                "commons-configuration:commons-configuration:jar:1.8",
                "org.uncommons.maths:uncommons-maths:jar:1.2.2",
                "org.apache.mahout.commons:commons-cli:jar:2.0-mahout",
                "commons-cli:commons-cli:jar:1.2",


                'org.apache.zookeeper:zookeeper:jar:3.3.3'
               ]


print("[" )
for i in DEPENDENCIES:
    splits = i.split(':')
    print("[" + splits[0]+ "/" + splits[1] + " \"" + splits[3] + "\"]")
print("]" )