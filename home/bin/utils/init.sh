V_PWD="$(cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"

source "$V_PWD/alias.sh"
export PYTHONPATH="$V_PWD:$PYTHONPATH"