import argparse
from .core import runBypassScan
import sys

def printBanner():
    print(r"""
          
███████╗██╗     ██╗██████╗ ██╗  ██╗ ██████╗ ██████╗ 
██╔════╝██║     ██║██╔══██╗██║  ██║██╔═████╗╚════██╗
███████╗██║     ██║██████╔╝███████║██║██╔██║ █████╔╝
╚════██║██║     ██║██╔═══╝ ╚════██║████╔╝██║ ╚═══██╗
███████║███████╗██║██║          ██║╚██████╔╝██████╔╝
╚══════╝╚══════╝╚═╝╚═╝          ╚═╝ ╚═════╝ ╚═════╝ 
                                                     v1.0
             403 Bypass Scanner | moth0xDEADBEEF
          
    This 


    """)
    

    def printBio():
        print("""
          Contribute: https://github.com/moth0xDEADBEEF/Slip403
          Buy me a coffee: 
    """)


def parseArguments():
    parser = argparse.ArgumentParser(description="403 Bypass Scanner")
    parser.add_argument("--url", required=True, help="Target base URL (e.g. https://example.com)")
    parser.add_argument("--path", required=True, help="Path to test (e.g. admin)")
    parser.add_argument("--delay", type=float, default=0.3, help="Delay between requests in seconds")
    parser.add_argument("--methods", default="GET,POST,TRACE", help="Comma-separated list of HTTP methods")
    parser.add_argument("--output", default="bypass_log.csv", help="Output CSV file")
    parser.add_argument("--save-responses", action="store_true", help="Save 200 responses that differ from baseline")
    parser.add_argument("--compare-baseline", action="store_true", help="Compare against baseline request")
    parser.add_argument("--hash-responses", action="store_true", help="Enable SHA256 hashing of response bodies")
    return parser.parse_args()

def main():
    printBanner()
    args = parseArguments()
    runBypassScan(
        baseUrl=args.url.strip("/"),
        basePath=args.path.strip("/"),
        delay=args.delay,
        methods=[m.strip().upper() for m in args.methods.split(",")],
        outputFile=args.output,
        saveResponses=args.save_responses,
        compareBaseline=args.compare_baseline,
        hashResponses=args.hash_responses
    )

if __name__ == "__main__":
    main()