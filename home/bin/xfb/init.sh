V_PWD="$(cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"

source "$V_PWD/alias.sh"
source "$V_PWD/env.sh"

export PYTHONPATH="$HOME/bin:$V_PWD:$PYTHONPATH"
