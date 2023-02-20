import argparse

def main(args):
    print(args.train)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="NLP ")
    parser.add_argument('-b', dest="bootstrap_servers", required=False,
                        help="Bootstrap broker(s) (host[:port])", default="pkc-3w22w.us-central1.gcp.confluent.cloud:9092")
    parser.add_argument('-s', dest="schema_registry", required=False,
                        help="Schema Registry (http(s)://host[:port]",default="https://psrc-mw0d1.us-east-2.aws.confluent.cloud")
    parser.add_argument('-t', dest="train", required=True default="rss_topic",
                        help="Topic name")
    parser.add_argument('-g', dest="group", default="example_serde_protobuf",
                        help="Consumer group")

    main(parser.parse_args())