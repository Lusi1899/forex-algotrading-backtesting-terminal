import React from 'react'
import AccountSummary from'../components/AccountSummary'
import Headlines from'../components/Headlines'
function Button({text, handleClick}) {
return(

<div>
<button onClick={()=> handleClick()}>{text}</button>
</div>

)
}

export default Button