import discord
import asyncio


import requests
from oci.config import from_file
from oci.signer import Signer


client = discord.Client()
token = "MTAwMzYwNDMxODQ0NTkwODAzOQ.GcKc2Y.vgVwqVtcSL-SwJq-fTQvJLo9V44fxI0R4zDpuY"


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    successcount = 0
    befleg = 0
    nowleg = 0


    nowleg = listit()
    befleg = nowleg


    while True:
        
        channel = client.get_channel(1003604857405575182)
        count = 0
        with open("count.txt", "r") as f:
            for line in f:
                count = int(line.strip())

        print(count)
        
        if successcount <=1:
            await channel.send(str(count) + "번째 시도중.. "+str(successcount)+"번 성공")
            fff = makeit()
            await channel.send(fff)

            nowleg = listit()

            if nowleg != befleg:
                await channel.send(str(count) + "번째 성공!  " + "@everyone")
                successcount += 1
                befleg = nowleg
            count+=1

        f = open("count.txt", 'w')
        f.write(str(count))
        f.close()
        await asyncio.sleep(30)








def listit():
    # configuration file 불러오기
    #config = from_file('C:\\Users\\H\\Desktop\\oraclepp\\oracleidentitycloudservice_hsjjace77-08-01-13-01.pem', "DEFAULT")

    # request의 auth 부분 생성
    auth = Signer(
	tenancy="ocid1.tenancy.oc1..aaaaaaaakadgkyqp3tm3vtikg5p36wcnjnbouw2wx4nt4jjcqucdfkv7ql3q",
        user="ocid1.user.oc1..aaaaaaaa23bldmqfse5c4mubl2rpagfpq4wnt2ypzjp2idn53unbk4z3ohmq",
        fingerprint="12:07:aa:e8:7a:8a:1e:b1:48:6d:0e:09:1e:6f:01:04",
        private_key_file_location="oracleidentitycloudservice_hsjjace77-08-01-13-01.pem"
    )

    # endpoint
    endpoint = 'https://iaas.ap-chuncheon-1.oraclecloud.com/20160918/instances/'

    # body
    body = {
      	"compartmentId":"ocid1.compartment.oc1..aaaaaaaamkvyeyq7dwa3dzsuamzppplcpdviwwdwfzq3kbosemhvidmxg7hq"
    }

    # request 보내기, 해당 API는 get method를 요구합니다.
    response = requests.get(endpoint, params=body, auth=auth)
    
    # 대충 instance 갯수가 0인 compartment에 만들고 길이로 판별하겠습니다.
    print(response.json())
    return len(response.json())

def makeit():
    # configuration file 불러오기
    #config = from_file("<configuration_file_경로>", "DEFAULT")

    # request의 auth 부분 생성
    auth = Signer(
	tenancy="ocid1.tenancy.oc1..aaaaaaaakadgkyqp3tm3vtikg5p36wcnjnbouw2wx4nt4jjcqucdfkv7ql3q",
        user="ocid1.user.oc1..aaaaaaaa23bldmqfse5c4mubl2rpagfpq4wnt2ypzjp2idn53unbk4z3ohmq",
        fingerprint="12:07:aa:e8:7a:8a:1e:b1:48:6d:0e:09:1e:6f:01:04",
        private_key_file_location="oracleidentitycloudservice_hsjjace77-08-01-13-01.pem"
    )
	

    # endpoint
    endpoint = 'https://iaas.ap-chuncheon-1.oraclecloud.com/20160918/instances/'

    # body
    body = {"metadata":{},"shape":"VM.Standard.A1.Flex","compartmentId":"ocid1.tenancy.oc1..aaaaaaaakadgkyqp3tm3vtikg5p36wcnjnbouw2wx4nt4jjcqucdfkv7ql3q","displayName":"instance-20220801-2203","availabilityDomain":"xpcb:AP-CHUNCHEON-1-AD-1","sourceDetails":{"sourceType":"image","imageId":"ocid1.image.oc1.ap-chuncheon-1.aaaaaaaat4c7qhin3nizrh3bljfnh2tjrrcwc6gwdazli3rwzli2mgd4tpca"},"isPvEncryptionInTransitEnabled":True,"createVnicDetails":{"assignPublicIp":False,"subnetId":"ocid1.subnet.oc1.ap-chuncheon-1.aaaaaaaa2cclka6nroegki2gnlkdndy5hioh26exoj4kjqq2ojacvg7i6vpq","assignPrivateDnsRecord":True},"agentConfig":{"pluginsConfig":[{"name":"Vulnerability Scanning","desiredState":"DISABLED"},{"name":"Oracle Java Management Service","desiredState":"DISABLED"},{"name":"Oracle Autonomous Linux","desiredState":"DISABLED"},{"name":"OS Management Service Agent","desiredState":"ENABLED"},{"name":"Compute Instance Run Command","desiredState":"ENABLED"},{"name":"Compute Instance Monitoring","desiredState":"ENABLED"},{"name":"Block Volume Management","desiredState":"DISABLED"},{"name":"Bastion","desiredState":"DISABLED"}],"isMonitoringDisabled":False,"isManagementDisabled":False},"definedTags":{},"freeformTags":{},"instanceOptions":{"areLegacyImdsEndpointsDisabled":False},"availabilityConfig":{"recoveryAction":"RESTORE_INSTANCE"},"shapeConfig":{"ocpus":2,"memoryInGBs":12}}

    # request 보내기, 해당 API는 post method를 요구합니다.
    response = requests.post(endpoint, json=body, auth=auth)
    print(response.json())
    return response.json()
    
client.run(token)