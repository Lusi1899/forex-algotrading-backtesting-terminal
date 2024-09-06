import endPoints from "../app/api"
import React, {useEffect,useState} from 'react'
import TitleHead from './TitleHead'
import Headline from './Headline'
function Headlines() {


    const[headlines,setHeadlines]= useState(null);

    useEffect(() => {
    loadHeadlines();
    },[])

    const loadHeadlines = async () => {
     const data = await endPoints.headlines();
    setHeadlines(data);

    }

return(

<div>
<TitleHead title= "Headlines" />
<div className="headbox">
<div className="segment grid">
{
headlines && headlines.map((item,index)=>{
return <Headline key={index} data={item} />
})
}
</div>
</div>
</div>

)
}

export default Headlines