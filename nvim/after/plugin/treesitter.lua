local status, treesitter = pcall(require, "nvim-treesitter.configs")
if not status then
    print("Nvim Treesitter is not installed")
end

treesitter.setup({
    ensure_installed = { "python", "json", "javascript", "go", "c", "lua", "rust", "typescript" },
    sync_install = false,
    auto_install = true,
    highlight = {
        enable = true,
        additional_vim_regex_highlighting = false,
    }
})
