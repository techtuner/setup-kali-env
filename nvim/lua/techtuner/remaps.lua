local keymap = vim.keymap.set
local opts = { silent = true }
local builtins = require("telescope.builtin")

vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- Telescope
keymap("n", "<leader>ff", ":Telescope find_files<cr>", opts)
keymap("n", "<C-p>", ":Telescope git_files<cr>", opts)

-- Nvim Tree
keymap("n", "<C-t>", ":NvimTreeToggle<cr>", opts)


-- Split Windows
keymap("n", "<leader>sv", "<C-w>v", opts) -- Split vertically
keymap("n", "<leader>sh", "<C-w>s", opts) -- Split horizontally
keymap("n", "<ledaer>se", "<C-w>=", opts) -- Split equally
keymap("n", "<leader>sx", ":close<CR>", opts)

-- Quit Vim
keymap("n", "<leader>q", ":q!<CR>", opts) -- Force Quit
keymap("n", "<leader>w", ":wq<CR>", opts) -- Save and Quit

-- Window Navigation
keymap("n", "<C-h>", "<C-w>h", opts)
keymap("n", "<C-j>", "<C-w>j", opts)
keymap("n", "<C-k>", "<C-w>k", opts)
keymap("n", "<C-l>", "<C-w>l", opts)

-- Ctrl+S to Save
keymap("n", "<C-S>", ":update<CR>", opts)
keymap("v", "<C-S>", "<C-C>:update<CR>", opts)
keymap("i", "<C-S>", "<C-O>:update<CR>", opts)

-- Transparency Toggle
keymap("n", "<leader>t", ":TransparentToggle<cr>", opts)

-- UndoTree
keymap("n", "<leadear>u", ":UndotreeToggle<cr>", opts)

-- Mason
keymap("n", "<leadear>m", ":Mason<cr>", opts)

-- Markdown Preview
keymap("n","<C-m>",":MarkdownPreviewToggle<cr>",opts)
