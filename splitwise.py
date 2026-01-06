class SplitWise:

    def solution(self):

        payment_summary={
            "hari":1200,
            "vipin":1400,
            "jhon":1000,
            "vishnu":0,
            "tom":120,
            "avinash":0,
            "jini":0,
            "asok":0
        }

        amounts=payment_summary.values()

        individual_split=sum(amounts)/len(payment_summary)

        split_summary={k:individual_split-v for k,v in payment_summary.items()}

        print(split_summary)


split_instance=SplitWise()

split_instance.solution()