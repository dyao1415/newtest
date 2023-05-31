
def testIfStatements(input: int) -> int:
    if input:
        return 1
    else:
        return 0



def testRecursion(input: int, answer: int) -> int:
    if input == 1:
        return answer
    if input % 2 == 0:
        input = input // 2
        answer += 1
    else:
        input = 3 * input + 1
        answer += 1
    return testRecursion(input, answer)

if __name__ == "__main__":
    print(testRecursion(12, 0))