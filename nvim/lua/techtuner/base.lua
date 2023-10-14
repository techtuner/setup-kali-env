local set = vim.opt


set.number = true
set.relativenumber = true
set.wrap = false
set.ignorecase = true
set.smartcase = true
set.tabstop = 2
set.shiftwidth = 2
set.numberwidth = 4
set.mouse = "a"
set.expandtab = true
set.autoindent = true
set.smartindent = true
set.cursorline = false
set.backspace = "eol,indent,start"
set.fileencoding = "utf=8"
set.clipboard:append("unnamedplus")
set.updatetime = 10
set.termguicolors = true
set.background = "dark"
set.hlsearch = true
set.incsearch = true
set.showmode = false
set.signcolumn = "no"
set.laststatus = 0
set.splitbelow = true
set.splitright = true
set.iskeyword:append("-")
set.completeopt = "menu,menuone,noselect"
set.writebackup = false
set.pumheight = 10
set.scrolloff = 10
set.sidescrolloff = 10
set.cmdheight = 2
set.title = true
set.ruler = false

-- Adding 'q' as keybinding to close some of the plugins
vim.api.nvim_create_autocmd({ "FileType" }, {
    pattern = { "qf", "mason", "telescope", "help", "man", "lspinfo", "spectre_panel" },
    callback = function()
        vim.cmd([[
      nnoremap <silent> <buffer> q :close<CR>
      set nobuflisted
    ]])
    end,
})

-- Highlight Yanked (Copied) Text
vim.api.nvim_create_autocmd({ "TextYankPost" }, {
    callback = function()
        vim.highlight.on_yank({ higroup = "visual", timeout = 200 })
    end,
})

-- Set wrap and spell in markdown and gitcommit
vim.api.nvim_create_autocmd({ "FileType" }, {
    pattern = { "gitcommit", "markdown" },
    callback = function()
        vim.opt_local.wrap = true
        vim.opt_local.spell = true
    end,
})

vim.cmd [[ set list listchars=eol:$ ]]
