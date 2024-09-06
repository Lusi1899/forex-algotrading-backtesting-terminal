import React from 'react'
import AccountSummary from'../components/AccountSummary'
import Headlines from'../components/Headlines'
function Headline({data}) {
return(

<div className="headline">
 <a href={data.link} target="_blank" rel="noreferrer">
 {data.headline}
 </a>
 </div>

)
}

export default Headline