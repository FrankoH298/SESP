(this["webpackJsonpsesp-frontend"]=this["webpackJsonpsesp-frontend"]||[]).push([[0],{222:function(e,t,a){"use strict";a.r(t);var c=a(1),s=a.n(c),n=a(82),r=a.n(n),l=(a(90),a(53),a(11)),i=a(49),o=a.n(i),d=a(0),j=function(){function e(){localStorage.removeItem("id_token")}return Object(c.useEffect)((function(){var e=document.querySelectorAll(".sidenav");o.a.Sidenav.init(e),e=document.querySelectorAll(".dropdown-trigger"),o.a.Dropdown.init(e)})),Object(d.jsxs)(d.Fragment,{children:[Object(d.jsx)("ul",{id:"dropdown1",className:"dropdown-content",children:null==localStorage.getItem("id_token")?Object(d.jsx)("li",{children:Object(d.jsx)(l.b,{className:"teal-text",to:{pathname:"/login/"},children:"Iniciar Sesi\xf3n"})}):Object(d.jsx)("li",{children:Object(d.jsx)("a",{href:"/",onClick:e,children:"Logout"})})}),Object(d.jsx)("ul",{id:"dropdown2",className:"dropdown-content",children:null==localStorage.getItem("id_token")?Object(d.jsx)("li",{children:Object(d.jsx)(l.b,{className:"teal-text",to:{pathname:"/login/"},children:"Iniciar Sesi\xf3n"})}):Object(d.jsx)("li",{children:Object(d.jsx)("a",{href:"/",onClick:e,children:"Logout"})})}),Object(d.jsx)("nav",{className:"teal",children:Object(d.jsx)("div",{className:"container",children:Object(d.jsxs)("div",{className:"nav-wrapper",children:[Object(d.jsx)(l.b,{to:"/",className:"brand-logo",children:"SESP"}),Object(d.jsx)("a",{href:"menu","data-target":"mobile-demo",className:"sidenav-trigger",children:Object(d.jsx)("i",{className:"material-icons",children:"menu"})}),Object(d.jsxs)("ul",{className:"right hide-on-med-and-down",children:[Object(d.jsx)("li",{children:Object(d.jsxs)("a",{href:"/",children:[Object(d.jsx)("i",{className:"material-icons right",children:"store"}),"Stores"]})}),Object(d.jsx)("li",{children:Object(d.jsxs)("a",{href:"perfil",className:"dropdown-trigger","data-target":"dropdown1",children:[Object(d.jsx)("i",{className:"material-icons right",children:"arrow_drop_down"}),"Perfil"]})})]})]})})}),Object(d.jsxs)("ul",{className:"sidenav",id:"mobile-demo",children:[Object(d.jsx)("li",{children:Object(d.jsxs)("a",{href:"/",children:[Object(d.jsx)("i",{className:"material-icons right",children:"store"}),"stores"]})}),Object(d.jsx)("li",{children:Object(d.jsxs)("a",{href:"perfil",className:"dropdown-trigger","data-target":"dropdown2",children:[Object(d.jsx)("i",{className:"material-icons right",children:"arrow_drop_down"}),"Perfil"]})})]})]})},b=a(4),h=a.p+"static/media/background.9c1ef017.jpeg",m=function(e){return Object(d.jsx)(d.Fragment,{children:Object(d.jsx)("div",{className:"col s12 m6 l6",children:Object(d.jsxs)("div",{className:"card",children:[Object(d.jsxs)("div",{className:"card-image waves-effect waves-block waves-light",children:[Object(d.jsx)("img",{className:"activator",src:h})," "]}),Object(d.jsxs)("div",{className:"card-content",children:[Object(d.jsxs)("span",{className:"card-title activator grey-text text-darken-4",children:[e.name,Object(d.jsx)("i",{className:"material-icons right",children:"more_vert"})]}),Object(d.jsx)(l.b,{className:"teal-text",to:{pathname:"/store/",state:{storeProps:e}},children:"M\xe1s Informaci\xf3n"})]}),Object(d.jsxs)("div",{className:"card-reveal",children:[Object(d.jsxs)("span",{className:"card-title grey-text text-darken-4",children:[e.name,Object(d.jsx)("i",{className:"material-icons right",children:"close"})]}),Object(d.jsxs)("p",{children:["Cantidad M\xe1xima: ",e.maxPeople]}),Object(d.jsxs)("p",{children:["Personas en el local: ",e.actualPeople]}),Object(d.jsxs)("p",{children:["Tel\xe9fono: ",e.telephoneNumber]}),Object(d.jsxs)("p",{children:["Direcci\xf3n: ",e.address]})]})]})})})},O=a(9),x=a.n(O),u=function(){var e=Object(c.useState)([]),t=Object(b.a)(e,2),a=t[0],s=t[1];return Object(c.useEffect)((function(){x.a.get("/api/stores/").then((function(e){s(e.data),console.log(e.data)})).catch((function(e){console.log(e)}))}),[]),Object(d.jsx)(d.Fragment,{children:Object(d.jsx)("div",{className:"container",children:Object(d.jsx)("div",{className:"row",children:a.map((function(e){return Object(d.jsx)("div",{children:Object(d.jsx)(m,{user:e.user,id:e.id,name:e.name,maxPeople:e.max_people,actualPeople:e.actual_people,telephoneNumber:e.telephone_number,isFull:e.is_full,address:e.address})},e.user)}))})})})},p=a(2);x.a.defaults.xsrfCookieName="csrftoken",x.a.defaults.xsrfHeaderName="X-CSRFToken";var f=function(){var e=Object(p.f)();var t=Object(c.useState)(null),a=Object(b.a)(t,2),s=a[0],n=a[1],r=Object(c.useState)(),l=Object(b.a)(r,2),i=l[0],o=l[1],j=Object(c.useState)(),h=Object(b.a)(j,2),m=h[0],O=h[1];return Object(d.jsx)(d.Fragment,{children:Object(d.jsx)("form",{onSubmit:function(t){var a={username:i,password:m};t.preventDefault(),x.a.post("/api-token-auth/",a).then((function(t){var a;a=t.data.token,localStorage.setItem("id_token",a),e.go(-1)})).catch((function(e){console.log(e),n(e.response.status)}))},children:Object(d.jsx)("div",{className:"row",style:{marginTop:"5rem"},children:Object(d.jsxs)("div",{className:"container",children:[Object(d.jsxs)("div",{className:"col s12 m6",children:[Object(d.jsxs)("div",{className:"input-field col s12",children:[Object(d.jsx)("input",{id:"username",name:"username",type:"text",className:"validate",onChange:function(e){o(e.target.value)}}),Object(d.jsx)("label",{htmlFor:"username",children:"Username"})]}),Object(d.jsxs)("div",{className:"input-field col s12",children:[Object(d.jsx)("input",{id:"password",type:"password",className:"validate",onChange:function(e){O(e.target.value)}}),Object(d.jsx)("label",{htmlFor:"password",children:"Contrase\xf1a"})]}),400===s?Object(d.jsx)("div",{className:"col s-12",children:Object(d.jsx)("div",{className:"card red darken-2",children:Object(d.jsx)("div",{className:"card-content",children:Object(d.jsx)("p",{className:"white-text",children:"Datos Incorrectos, por favor intente de nuevo."})})})}):""]}),Object(d.jsx)("button",{className:"waves-effect waves-light btn red",children:"Inciar Sesi\xf3n"})]})})})})},g=a(23),v=function(e){var t=Object(c.useState)([]),a=Object(b.a)(t,2),s=a[0],n=a[1],r=Object(c.useState)([]),l=Object(b.a)(r,2),i=l[0],o=l[1],j=Object(c.useState)([]),h=Object(b.a)(j,2),m=h[0],O=h[1],u=Object(c.useState)([]),p=Object(b.a)(u,2),f=p[0],v=p[1],N=Object(c.useState)(!1),w=Object(b.a)(N,2),k=w[0],_=w[1];Object(c.useEffect)((function(){x.a.get("/api/total_entries_last_week/"+e.store.id,{headers:{Authorization:"Token "+localStorage.getItem("id_token")}}).then((function(e){n(e.data)})).catch((function(e){_(!0)})),x.a.get("/api/total_entries_per_day/"+e.store.id,{headers:{Authorization:"Token "+localStorage.getItem("id_token")}}).then((function(e){o(e.data)})).catch((function(e){_(!0)})),x.a.get("/api/total_entries_per_hour_last_two_weeks/"+e.store.id,{headers:{Authorization:"Token "+localStorage.getItem("id_token")}}).then((function(e){v(e.data)})).catch((function(e){_(!0)})),x.a.get("/api/total_entries_per_month/"+e.store.id,{headers:{Authorization:"Token "+localStorage.getItem("id_token")}}).then((function(e){O(e.data)})).catch((function(e){_(!0)}))}),[]);var S={labels:Object.keys(s),datasets:[{label:"Cantidad de Ingresos por d\xeda",backgroundColor:"#00897b",borderColor:"#005249",fill:!0,data:Object.values(s)}]},I={labels:Object.keys(i),datasets:[{label:"Ingresos",backgroundColor:["#00897b","#185855","#8fe8df","#254dcb","#df1818","#9900ff","#ff00aa"],borderColor:"#ffffff",data:Object.values(i)}]},C={labels:Object.keys(m),datasets:[{label:"Ingresos",backgroundColor:["#69da86","#d72bdb","#7aef53","#5c128f","#20c1cb","#260046","#6f230e","#03590b","#29c152","#ea9c62","#0a4a3a","#205ba8"],borderColor:"#ffffff",data:Object.values(m)}]},y={labels:Object.keys(f),datasets:[{label:"Cantidad de Ingresos por hora",backgroundColor:"#00897b",borderColor:"#005249",fill:!0,data:Object.values(f)}]},F={elements:{line:{tension:.4}}};return k?Object(d.jsx)(d.Fragment,{}):Object(d.jsx)(d.Fragment,{children:Object(d.jsx)("div",{className:"row",children:Object(d.jsx)("div",{className:"container",children:Object(d.jsx)("div",{className:"col s12",children:Object(d.jsx)("div",{className:"card",children:Object(d.jsx)("div",{className:"card-content",children:Object(d.jsxs)("div",{className:"row",children:[Object(d.jsxs)("div",{className:"col s12 m6 l6 center-align",children:[Object(d.jsx)("span",{children:"Ingresos por d\xeda"}),Object(d.jsx)("div",{className:"App",children:Object(d.jsx)(g.b,{data:S,options:F})})]}),Object(d.jsxs)("div",{className:"col s12 m6 l6 center-align",children:[Object(d.jsx)("span",{children:" Ingresos por Mes"}),Object(d.jsx)("div",{children:Object(d.jsx)(g.a,{data:C})})]}),Object(d.jsxs)("div",{className:"col s12 m6 l6 center-align",children:[Object(d.jsx)("span",{children:"Cantidad de Ingresos por hora"}),Object(d.jsx)("div",{children:Object(d.jsx)(g.b,{data:y,options:F})})]}),Object(d.jsxs)("div",{className:"col s12 m4 l4 center-align",children:[Object(d.jsx)("span",{children:"D\xedas con mayores ingresos"}),Object(d.jsx)("div",{children:Object(d.jsx)(g.c,{data:I})})]})]})})})})})})})},N=function(){var e,t=Object(p.g)(),a=Object(c.useState)([]),s=Object(b.a)(a,2),n=s[0],r=s[1],l=null===(e=t.state)||void 0===e?void 0:e.storeProps,i=null,o=window.location.host,j=function e(){(i=new WebSocket("wss://"+o+"/ws/inicio/")).onmessage=function(e){var t=JSON.parse(e.data);r(t.key_value)},i.onopen=function(){i.send(l.id)},i.onclose=function(){setTimeout((function(){i=null,e()}),3e3)}};return Object(c.useEffect)((function(){return j(),function(){i.onclose=function(){},i.close()}}),[]),Object(d.jsxs)(d.Fragment,{children:[Object(d.jsx)("div",{className:"container",children:Object(d.jsx)("div",{className:"row center",children:Object(d.jsx)("div",{className:"col s12",children:Object(d.jsx)("div",{className:"row",children:Object(d.jsx)("div",{className:"col s12 m12",children:Object(d.jsxs)("div",{className:"card",children:[Object(d.jsx)("div",{className:"card-content",children:Object(d.jsx)("div",{className:"center-align",children:Object(d.jsx)("h3",{style:{margin:"0px"},children:n.name})})}),Object(d.jsx)("div",{className:"card-action teal center-align",children:Object(d.jsxs)("div",{className:"row",children:[Object(d.jsxs)("div",{className:"col s12 m6",children:[Object(d.jsx)("h5",{className:"white-text",children:"Capacidad M\xe1xima"}),Object(d.jsx)("h2",{className:"white-text",style:{margin:"0px"},children:n.max_people})]}),Object(d.jsxs)("div",{className:"col s12 m6",children:[Object(d.jsx)("h5",{className:"white-text",children:"Personas Actuales"}),Object(d.jsx)("h2",{className:"white-text",style:{margin:"0px"},children:n.actual_people})]})]})}),Object(d.jsx)("div",{className:"card-action"+(n.is_full?" red ":" green ")+"center-align",children:Object(d.jsx)("h2",{className:"white-text center-align",style:{margin:"0px"},children:n.is_full?"Lleno, no puedes pasar":"Puedes pasar"})})]})})})})})}),Object(d.jsx)(v,{store:l})]})};var w=function(){return Object(d.jsx)(d.Fragment,{children:Object(d.jsxs)(l.a,{children:[Object(d.jsx)(j,{}),Object(d.jsxs)(p.c,{children:[Object(d.jsx)(p.a,{path:"/login/",component:f}),Object(d.jsx)(p.a,{path:"/store/",component:N}),Object(d.jsx)(p.a,{path:"/",component:u,exact:!0})]})]})})};r.a.render(Object(d.jsx)(s.a.StrictMode,{children:Object(d.jsx)(w,{})}),document.getElementById("root"))},90:function(e,t,a){}},[[222,1,2]]]);
//# sourceMappingURL=main.4ee634f6.chunk.js.map