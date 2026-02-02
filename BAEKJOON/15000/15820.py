import sys

def main():
    input = sys.stdin.readline
    s1, s2 = map(int, input().split())

    # 샘플 테스트케이스 검사
    for _ in range(s1):
        a, b = input().split()
        if a != b:  # 문자열로 비교해도 되고
            print("Wrong Answer")
            return

    # 시스템 테스트케이스 검사 (샘플은 모두 맞은 상태)
    for _ in range(s2):
        a, b = input().split()
        if a != b:
            print("Why Wrong!!!")
            return

    print("Accepted")

if __name__ == "__main__":
    main()
