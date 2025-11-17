"""
【スクリプトの目的】
・ディスク使用率チェック
・df -h や /proc を見て、閾値超えたらログ出力＋終了コード1で終了。
【実装方針】
    # 1. ディスク使用率を取得
    # 2. しきい値と比較
    # 3. 超えていた場合はログ出力
    # 4. 終了コード1で終了
"""
import shutil
import sys


threshold = 80  # ディスク使用率の閾値（％）

def check_disk_usage(threshold: int) -> int:
    usage = get_disk_usage()
    issues = compare_usage(usage, threshold)
    if issues:
        log_exceeded(issues)
        return 1
    return 0

def get_disk_usage() -> dict:
    # ディスク使用率を取得するロジック 
    total, used, free = shutil.disk_usage("/")
    usage = used / total * 100
    return {"total": total, "used": used, "free": free, "usage": usage}

def compare_usage(usage: dict, threshold: int) -> list:
    # 使用率と閾値を比較し、超えている場合はリストに追加
    issues = []
    if usage["usage"] > threshold:
        issues.append(usage)
    return issues

def log_exceeded(issues: list) -> None:
    # 超えているディスク使用率をログに出力
    for usage in issues:
        print(f"Disk usage exceeded: {usage['usage']:.2f}%")

if __name__ == "__main__":
    sys.exit(check_disk_usage(threshold))
