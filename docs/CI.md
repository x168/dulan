# PR 文件驗證

PR 的 `PR contract and documents` 檢查使用自架 Linux 容器 runner。
workflow 為 [.github/workflows/pr-validation.yml](../.github/workflows/pr-validation.yml)，
要求 `home-linux`、`home-amd64` 與每個 job 唯一的 `slot-*` 標籤。
CI 控制器負責供應 runner；開發工作站不執行驗證。

每次開啟、更新、重新開啟、轉為可審查或編輯 PR，都會驗證相同的完整 head SHA。
檢查包括差異空白、契約回歸測試、禁止追蹤路徑、文字編碼與換行、相對文件連結，
以及 PR 聲明與所連結 Issue 的即時分類、里程碑和六個必要段落。
`Closes` 只能連結尚未關閉的 Issue；仍須保留 Issue 時使用 `Tracks`。

CI 指令：

```sh
python3 -m unittest discover -s scripts/ci -p 'test_*.py' -v
python3 scripts/ci/check_documents.py
python3 scripts/ci/validate_pr_contract.py
```

契約工具也接受 `--body-file <檔案>`，供自架 CI 驗證準備好的 PR 本文。
它需要唯讀 `GH_TOKEN`，透過 GitHub REST 讀取 Issue，不使用 GraphQL。
PR 範本見 [.github/pull_request_template.md](../.github/pull_request_template.md)。
目前的 parser 不查核外部網站的連線、Markdown 錨點或完整 ASD-STE100 標準符合性；
文件連結與寫作品質仍須人工審閱。檢查成功也不代表網站已建置或部署。

當 runner 尚未供應或檢查缺少時，PR 保持開啟。
實際供應與驗證證據由 [Issue #2](https://github.com/x168/dulan/issues/2) 追蹤。
本文件描述 workflow 行為；任務、擁有權與合併規則以 [AGENTS.md](../AGENTS.md) 為準。
