-- Packer https://github.com/wbthomason/packer.nvim : Plugin Manager

local ensure_packer = function()
    local fn = vim.fn
    local install_path = fn.stdpath('data') .. '/site/pack/packer/start/packer.nvim'
    if fn.empty(fn.glob(install_path)) > 0 then
        fn.system({ 'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path })
        vim.cmd [[packadd packer.nvim]]
        return true
    end
    return false
end

local packer_bootstrap = ensure_packer()

vim.cmd([[
  augroup packer_user_config
    autocmd!
    autocmd BufWritePost plugins.lua source <afile> | PackerCompile
  augroup end
]])

local status, packer = pcall(require, "packer")
if not status then
    print("Packer is not installed")
    return
end

packer.init({
    display = {
        open_fn = function()
            return require("packer.util").float({
                border = 'rounded'
            })
        end
    }
})

return require('packer').startup(function(use)
    -- Packer install itself
    use('wbthomason/packer.nvim')

    -- Required Plugins
    use("nvim-lua/plenary.nvim")
    use("kyazdani42/nvim-web-devicons")
    use("nvim-lua/popup.nvim")

    -- Nvim Tree : File aexplorer
    use("nvim-tree/nvim-tree.lua")

    -- Telescope : Fuzzy finder
    use({ "nvim-telescope/telescope.nvim", branch = '0.1.x' })
    use("nvim-telescope/telescope-media-files.nvim")

    -- Undo Tree : Visualize Undo History
    use('mbbill/undotree')

    -- Treesitter : Syntax Available
    use({ "nvim-treesitter/nvim-treesitter", run = ":TSUpdate" })
    use("windwp/nvim-autopairs")
    use("windwp/nvim-ts-autotag")

    -- Colorscheme
    --use('techtuner/nord.nvim')
    use('catppuccin/nvim')
    -- GitSigns
    use("lewis6991/gitsigns.nvim")

    -- Which key
    use("folke/which-key.nvim")

    -- Lsp : Language Support
    use({
        'VonHeikemen/lsp-zero.nvim',
        branch = 'v2.x',
        requires = {
            -- LSP Support
            { 'williamboman/mason.nvim' },
            { 'williamboman/mason-lspconfig.nvim' },
            { 'neovim/nvim-lspconfig' },

            -- Autocompletion
            { 'hrsh7th/nvim-cmp' },
            { 'hrsh7th/cmp-buffer' },
            { 'hrsh7th/cmp-path' },
            { 'saadparwaiz1/cmp_luasnip' },
            { 'hrsh7th/cmp-nvim-lsp' },
            { 'hrsh7th/cmp-nvim-lua' },

            -- Snippets
            { 'L3MON4D3/LuaSnip' },
            { 'rafamadriz/friendly-snippets' },
        }
    })

    -- Transparency neovim
    use("xiyaowong/transparent.nvim")


    -- Markdown preview
    use({
        "iamcco/markdown-preview.nvim",
        run = "cd app && npm install",
        setup = function() vim.g.mkdp_filetypes = { "markdown" } end,
        ft = { "markdown" },
    })

    if packer_bootstrap then
        require('packer').sync()
    end
end)
