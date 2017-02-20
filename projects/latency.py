"""
Question:
Pick one IP from each region, find network latency from via the below code snippet
(ping 3 times), and finally sort regions by the average latency.
http://ec2-reachability.amazonaws.com/
Sample output:
1. us-west-1 [50.18.56.1] - Smallest average latency
2. xx-xxxx-x [xx.xx.xx.xx] - x
3. xx-xxxx-x [xx.xx.xx.xx] - x
...
15. xx-xxxx-x [xx.xx.xx.xx] - Largest average latency
"""
import subprocess

host_list = {"54.191.63.252": "us-west-2", "54.243.255.254": "us-east-1", "52.222.9.163": "us-gov-west-1",
             "54.93.162.162": "eu-central-1", "52.66.66.2": "ap-south-1", "54.207.127.254": "sa-east-1",
             "13.112.63.251": "ap-northeast-1", "46.51.255.254": "ap-northeast-1", "52.78.63.252": "ap-northeast-2",
             "46.137.255.254": "ap-southeast-1", "13.54.63.252": "ap-southeast-2", "52.64.191.252": "ap-southeast-2",
             "35.154.63.252": "ap-south-1", "52.60.50.0": "ca-central-1"}


def process_iterate(values_dict):
    results_dict = {}
    for ip in values_dict:
        ping = subprocess.Popen(["ping", "-c", "3", ip],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        out, error = ping.communicate()
        # split along new line,get last 3 lines of output;split to find required..
        out = out.split('\n')[-4:]
        ip_address = out[0].split(" ")[1]
        timing_stats = out[2].split("=")[1].split("/")
        average_latency = float(timing_stats[1])
        results_dict[values_dict[ip_address] + " [" + ip_address + "]"] = average_latency

    return results_dict


results = process_iterate(host_list)
sorted_results = sorted(results.items(), key=lambda x: x[1])

for i in sorted_results:
    print (i[0], " ", i[1])
