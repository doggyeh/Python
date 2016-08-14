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
set showmode
set showmatch
set background=dark
set backspace=2
set cursorline!
set tabstop=2
set shiftwidth=2
set softtabstop=2
set smarttab
set expandtab
set fileformat=unix
set statusline+=%F
set laststatus=2
syntax on
set nocompatible
filetype off

let g:ycm_autoclose_preview_window_after_completion=1
nnoremap <leader>g :YcmCompleter GoToDefinitionElseDeclaration<CR>

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'gmarik/Vundle.vim'
Bundle 'Valloric/YouCompleteMe'
call vundle#end()
filetype plugin indent on

" copy to buffer
vmap <C-c> :w! ~/.vimbuffer<CR>
nmap <C-c> :.w! ~/.vimbuffer<CR>
" paste from buffer
map <C-v> :r ~/.vimbuffer<CR>
