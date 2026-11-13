# Safe GitHub Publishing Checklist

1. Use the independent **PORTFOLIO_PUBLIC** folder, not any production/workplace application directory.
2. Open `README.md` and `src/order_check_demo.py` to confirm they contain only generic demo information.
3. Verify the absence of real customer data, order spreadsheets, databases, logs, tokens, passwords, private keys, company branding, and private business documentation.
4. Create a repository such as `ecommerce-order-checking-system` on GitHub.
5. Upload the **contents of the extracted folder**, not the ZIP archive itself. Keep `README.md` at the repository root.
6. Use the short description from `GITHUB_DESCRIPTION.txt` and add the suggested topics if desired.
7. Review the selected files once more before clicking **Commit changes**.
8. Choose Public only if you are satisfied all included content is independently created and shareable. Otherwise keep it Private.

Note: `.gitignore` prevents some common files from being added, but cannot protect secrets that have already been committed.
