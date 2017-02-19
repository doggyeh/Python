"let GtagsCscope_Auto_Map = 1
"let GtagsCscope_Auto_Load = 1
"let GtagsCscope_Quiet = 1
"set cscopetag

set listchars=tab:>-,trail:~,extends:>,precedes:<
set list
set nu
set hlsearch
set autoindent
set ruler
set showmode
set showmatch
set backspace=2
set cursorline!
set tabstop=2
set shiftwidth=2
set softtabstop=2
set smarttab
set expandtab
set fileformat=unix
set laststatus=2
set statusline=%<%F\ %h%m%r%y%=%-14.(%l,%c%V%)\ %P
set relativenumber
set scrolloff=10
autocmd FileType sh,zsh,python,perl,ruby match ErrorMsg '\%>80v.\+'
execute pathogen#infect()
syntax on
syntax enable
set background=dark
let g:solarized_termcolors=256
colorscheme solarized
set nocompatible
filetype off

let g:ycm_autoclose_preview_window_after_completion=1
nnoremap <leader>g :YcmCompleter GoToDefinitionElseDeclaration<CR>

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
Plugin 'terryma/vim-smooth-scroll'
Bundle 'Valloric/YouCompleteMe'
call vundle#end()
filetype plugin indent on

" copy to buffer
vmap <C-c> :w! ~/.vimbuffer<CR>
nmap <C-c> :.w! ~/.vimbuffer<CR>
" paste from buffer
map <C-v> :r ~/.vimbuffer<CR>

"Fuzzy Finder
set rtp+=~/.fzf

noremap <silent> <c-u> :call smooth_scroll#up(&scroll, 0, 2)<CR>
noremap <silent> <c-d> :call smooth_scroll#down(&scroll, 0, 2)<CR>
noremap <silent> <c-b> :call smooth_scroll#up(&scroll*2, 0, 4)<CR>
noremap <silent> <c-f> :call smooth_scroll#down(&scroll*2, 0, 4)<CR>

set mouse=n
autocmd FileType c,cpp,java,verilog noremap <silent>. :s:^\(\s*\):\1// :<CR>:noh<CR>
autocmd FileType c,cpp,java,verilog noremap <silent>, :s:^\(\s*\)// :\1:<CR>:noh<CR>
autocmd FileType sh,zsh,python,perl,ruby noremap <silent>. :s:^\(\s*\):\1# :<CR>:noh<CR>
autocmd FileType sh,zsh,python,perl,ruby noremap <silent>, :s:^\(\s*\)# :\1:<CR>:noh<CR>
autocmd FileType vim noremap <silent>. :s:^\(\s*\):\1" :<CR>:noh<CR>
autocmd FileType vim noremap <silent>, :s:^\(\s*\)" :\1:<CR>:noh<CR>
autocmd FileType asm noremap <silent>. :s:^\(\s*\):\1; :<CR>:noh<CR>
autocmd FileType asm noremap <silent>, :s:^\(\s*\); :\1:<CR>:noh<CR>
autocmd FileType vhdl,sql noremap <silent>. :s:^\(\s*\):\1-- :<CR>:noh<CR>
autocmd FileType vhdl,sql noremap <silent>, :s:^\(\s*\)-- :\1:<CR>:noh<CR>
