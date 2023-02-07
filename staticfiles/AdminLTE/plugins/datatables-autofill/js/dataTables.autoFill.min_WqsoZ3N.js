/*!
   Copyright 2010-2021 SpryMedia Ltd.

 This source file is free software, available under the following license:
   MIT license - http://datatables.net/license/mit

 This source file is distributed in the hope that it will be useful, but
 WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 or FITNESS FOR A PARTICULAR PURPOSE. See the license files for details.

 For details please refer to: http://www.datatables.net
 AutoFill 2.3.9
 ©2008-2021 SpryMedia Ltd - datatables.net/license
*/
var $jscomp=$jscomp||{};$jscomp.scope={};$jscomp.arrayIteratorImpl=function(c){var h=0;return function(){return h<c.length?{done:!1,value:c[h++]}:{done:!0}}};$jscomp.arrayIterator=function(c){return{next:$jscomp.arrayIteratorImpl(c)}};$jscomp.ASSUME_ES5=!1;$jscomp.ASSUME_NO_NATIVE_MAP=!1;$jscomp.ASSUME_NO_NATIVE_SET=!1;$jscomp.SIMPLE_FROUND_POLYFILL=!1;$jscomp.ISOLATE_POLYFILLS=!1;
$jscomp.defineProperty=$jscomp.ASSUME_ES5||"function"==typeof Object.defineProperties?Object.defineProperty:function(c,h,g){if(c==Array.prototype||c==Object.prototype)return c;c[h]=g.value;return c};$jscomp.getGlobal=function(c){c=["object"==typeof globalThis&&globalThis,c,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var h=0;h<c.length;++h){var g=c[h];if(g&&g.Math==Math)return g}throw Error("Cannot find global object");};$jscomp.global=$jscomp.getGlobal(this);
$jscomp.IS_SYMBOL_NATIVE="function"===typeof Symbol&&"symbol"===typeof Symbol("x");$jscomp.TRUST_ES6_POLYFILLS=!$jscomp.ISOLATE_POLYFILLS||$jscomp.IS_SYMBOL_NATIVE;$jscomp.polyfills={};$jscomp.propertyToPolyfillSymbol={};$jscomp.POLYFILL_PREFIX="$jscp$";var $jscomp$lookupPolyfilledValue=function(c,h){var g=$jscomp.propertyToPolyfillSymbol[h];if(null==g)return c[h];g=c[g];return void 0!==g?g:c[h]};
$jscomp.polyfill=function(c,h,g,k){h&&($jscomp.ISOLATE_POLYFILLS?$jscomp.polyfillIsolated(c,h,g,k):$jscomp.polyfillUnisolated(c,h,g,k))};$jscomp.polyfillUnisolated=function(c,h,g,k){g=$jscomp.global;c=c.split(".");for(k=0;k<c.length-1;k++){var l=c[k];if(!(l in g))return;g=g[l]}c=c[c.length-1];k=g[c];h=h(k);h!=k&&null!=h&&$jscomp.defineProperty(g,c,{configurable:!0,writable:!0,value:h})};
$jscomp.polyfillIsolated=function(c,h,g,k){var l=c.split(".");c=1===l.length;k=l[0];k=!c&&k in $jscomp.polyfills?$jscomp.polyfills:$jscomp.global;for(var y=0;y<l.length-1;y++){var r=l[y];if(!(r in k))return;k=k[r]}l=l[l.length-1];g=$jscomp.IS_SYMBOL_NATIVE&&"es6"===g?k[l]:null;h=h(g);null!=h&&(c?$jscomp.defineProperty($jscomp.polyfills,l,{configurable:!0,writable:!0,value:h}):h!==g&&($jscomp.propertyToPolyfillSymbol[l]=$jscomp.IS_SYMBOL_NATIVE?$jscomp.global.Symbol(l):$jscomp.POLYFILL_PREFIX+l,l=
$jscomp.propertyToPolyfillSymbol[l],$jscomp.defineProperty(k,l,{configurable:!0,writable:!0,value:h})))};$jscomp.initSymbol=function(){};
$jscomp.polyfill("Symbol",function(c){if(c)return c;var h=function(l,y){this.$jscomp$symbol$id_=l;$jscomp.defineProperty(this,"description",{configurable:!0,writable:!0,value:y})};h.prototype.toString=function(){return this.$jscomp$symbol$id_};var g=0,k=function(l){if(this instanceof k)throw new TypeError("Symbol is not a constructor");return new h("jscomp_symbol_"+(l||"")+"_"+g++,l)};return k},"es6","es3");$jscomp.initSymbolIterator=function(){};
$jscomp.polyfill("Symbol.iterator",function(c){if(c)return c;c=Symbol("Symbol.iterator");for(var h="Array Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array".split(" "),g=0;g<h.length;g++){var k=$jscomp.global[h[g]];"function"===typeof k&&"function"!=typeof k.prototype[c]&&$jscomp.defineProperty(k.prototype,c,{configurable:!0,writable:!0,value:function(){return $jscomp.iteratorPrototype($jscomp.arrayIteratorImpl(this))}})}return c},"es6",
"es3");$jscomp.initSymbolAsyncIterator=function(){};$jscomp.iteratorPrototype=function(c){c={next:c};c[Symbol.iterator]=function(){return this};return c};$jscomp.iteratorFromArray=function(c,h){c instanceof String&&(c+="");var g=0,k={next:function(){if(g<c.length){var l=g++;return{value:h(l,c[l]),done:!1}}k.next=function(){return{done:!0,value:void 0}};return k.next()}};k[Symbol.iterator]=function(){return k};return k};
$jscomp.polyfill("Array.prototype.keys",function(c){return c?c:function(){return $jscomp.iteratorFromArray(this,function(h){return h})}},"es6","es3");
(function(c){"function"===typeof define&&define.amd?define(["jquery","datatables.net"],function(h){return c(h,window,document)}):"object"===typeof exports?module.exports=function(h,g){h||(h=window);g&&g.fn.dataTable||(g=require("datatables.net")(h,g).$);return c(g,h,h.document)}:c(jQuery,window,document)})(function(c,h,g,k){var l=c.fn.dataTable,y=0,r=function(a,d){if(!l.versionCheck||!l.versionCheck("1.10.8"))throw"Warning: AutoFill requires DataTables 1.10.8 or greater";this.c=c.extend(!0,{},l.defaults.autoFill,
r.defaults,d);this.s={dt:new l.Api(a),namespace:".autoFill"+y++,scroll:{},scrollInterval:null,handle:{height:0,width:0},enabled:!1};this.dom={handle:c('<div class="dt-autofill-handle"/>'),select:{top:c('<div class="dt-autofill-select top"/>'),right:c('<div class="dt-autofill-select right"/>'),bottom:c('<div class="dt-autofill-select bottom"/>'),left:c('<div class="dt-autofill-select left"/>')},background:c('<div class="dt-autofill-background"/>'),list:c('<div class="dt-autofill-list">'+this.s.dt.i18n("autoFill.info",
"")+"<ul/></div>"),dtScroll:null,offsetParent:null};this._constructor()};c.extend(r.prototype,{enabled:function(){return this.s.enabled},enable:function(a){var d=this;if(!1===a)return this.disable();this.s.enabled=!0;this._focusListener();this.dom.handle.on("mousedown",function(b){d._mousedown(b);return!1});return this},disable:function(){this.s.enabled=!1;this._focusListenerRemove();return this},_constructor:function(){var a=this,d=this.s.dt,b=c("div.dataTables_scrollBody",this.s.dt.table().container());
d.settings()[0].autoFill=this;b.length&&(this.dom.dtScroll=b,"static"===b.css("position")&&b.css("position","relative"));!1!==this.c.enable&&this.enable();d.on("destroy.autoFill",function(){a._focusListenerRemove()})},_attach:function(a){var d=this.s.dt,b=d.cell(a).index(),e=this.dom.handle,f=this.s.handle;b&&-1!==d.columns(this.c.columns).indexes().indexOf(b.column)?(this.dom.offsetParent||(this.dom.offsetParent=c(d.table().node()).offsetParent()),f.height&&f.width||(e.appendTo("body"),f.height=
e.outerHeight(),f.width=e.outerWidth()),d=this._getPosition(a,this.dom.offsetParent),this.dom.attachedTo=a,e.css({top:d.top+a.offsetHeight-f.height,left:d.left+a.offsetWidth-f.width}).appendTo(this.dom.offsetParent)):this._detach()},_actionSelector:function(a){var d=this,b=this.s.dt,e=r.actions,f=[];c.each(e,function(p,q){q.available(b,a)&&f.push(p)});if(1===f.length&&!1===this.c.alwaysAsk){var m=e[f[0]].execute(b,a);this._update(m,a)}else if(1<f.length){var n=this.dom.list.children("ul").empty();
f.push("cancel");c.each(f,function(p,q){n.append(c("<li/>").append('<div class="dt-autofill-question">'+e[q].option(b,a)+"<div>").append(c('<div class="dt-autofill-button">').append(c('<button class="'+r.classes.btn+'">'+b.i18n("autoFill.button","&gt;")+"</button>").on("click",function(){var v=e[q].execute(b,a,c(this).closest("li"));d._update(v,a);d.dom.background.remove();d.dom.list.remove()}))))});this.dom.background.appendTo("body");this.dom.list.appendTo("body");this.dom.list.css("margin-top",
this.dom.list.outerHeight()/2*-1)}},_detach:function(){this.dom.attachedTo=null;this.dom.handle.detach()},_drawSelection:function(a,d){var b=this.s.dt;d=this.s.start;var e=c(this.dom.start),f={row:this.c.vertical?b.rows({page:"current"}).nodes().indexOf(a.parentNode):d.row,column:this.c.horizontal?c(a).index():d.column};a=b.column.index("toData",f.column);var m=b.row(":eq("+f.row+")",{page:"current"});m=c(b.cell(m.index(),a).node());if(b.cell(m).any()&&-1!==b.columns(this.c.columns).indexes().indexOf(a)){this.s.end=
f;b=d.row<f.row?e:m;var n=d.row<f.row?m:e;a=d.column<f.column?e:m;e=d.column<f.column?m:e;b=this._getPosition(b.get(0)).top;a=this._getPosition(a.get(0)).left;d=this._getPosition(n.get(0)).top+n.outerHeight()-b;e=this._getPosition(e.get(0)).left+e.outerWidth()-a;f=this.dom.select;f.top.css({top:b,left:a,width:e});f.left.css({top:b,left:a,height:d});f.bottom.css({top:b+d,left:a,width:e});f.right.css({top:b,left:a+e,height:d})}},_editor:function(a){var d=this.s.dt,b=this.c.editor;if(b){for(var e={},
f=[],m=b.fields(),n=0,p=a.length;n<p;n++)for(var q=0,v=a[n].length;q<v;q++){var u=a[n][q],w=d.settings()[0].aoColumns[u.index.column],t=w.editField;if(t===k){w=w.mData;for(var x=0,z=m.length;x<z;x++){var A=b.field(m[x]);if(A.dataSrc()===w){t=A.name();break}}}if(!t)throw"Could not automatically determine field data. Please see https://datatables.net/tn/11";e[t]||(e[t]={});w=d.row(u.index.row).id();e[t][w]=u.set;f.push(u.index)}b.bubble(f,!1).multiSet(e).submit()}},_emitEvent:function(a,d){this.s.dt.iterator("table",
function(b,e){c(b.nTable).triggerHandler(a+".dt",d)})},_focusListener:function(){var a=this,d=this.s.dt,b=this.s.namespace,e=null!==this.c.focus?this.c.focus:d.init().keys||d.settings()[0].keytable?"focus":"hover";if("focus"===e)d.on("key-focus.autoFill",function(f,m,n){a._attach(n.node())}).on("key-blur.autoFill",function(f,m,n){a._detach()});else if("click"===e)c(d.table().body()).on("click"+b,"td, th",function(f){a._attach(this)}),c(g.body).on("click"+b,function(f){c(f.target).parents().filter(d.table().body()).length||
a._detach()});else c(d.table().body()).on("mouseenter"+b,"td, th",function(f){a._attach(this)}).on("mouseleave"+b,function(f){c(f.relatedTarget).hasClass("dt-autofill-handle")||a._detach()})},_focusListenerRemove:function(){var a=this.s.dt;a.off(".autoFill");c(a.table().body()).off(this.s.namespace);c(g.body).off(this.s.namespace)},_getPosition:function(a,d){var b=0,e=0;d||(d=c(c(this.s.dt.table().node())[0].offsetParent));do{var f=a.offsetTop,m=a.offsetLeft;var n=c(a.offsetParent);b+=f+1*parseInt(n.css("border-top-width")||
0);e+=m+1*parseInt(n.css("border-left-width")||0);if("body"===a.nodeName.toLowerCase())break;a=n.get(0)}while(n.get(0)!==d.get(0));return{top:b,left:e}},_mousedown:function(a){var d=this,b=this.s.dt;this.dom.start=this.dom.attachedTo;this.s.start={row:b.rows({page:"current"}).nodes().indexOf(c(this.dom.start).parent()[0]),column:c(this.dom.start).index()};c(g.body).on("mousemove.autoFill",function(f){d._mousemove(f)}).on("mouseup.autoFill",function(f){d._mouseup(f)});var e=this.dom.select;b=c(b.table().node()).offsetParent();
e.top.appendTo(b);e.left.appendTo(b);e.right.appendTo(b);e.bottom.appendTo(b);this._drawSelection(this.dom.start,a);this.dom.handle.css("display","none");a=this.dom.dtScroll;this.s.scroll={windowHeight:c(h).height(),windowWidth:c(h).width(),dtTop:a?a.offset().top:null,dtLeft:a?a.offset().left:null,dtHeight:a?a.outerHeight():null,dtWidth:a?a.outerWidth():null}},_mousemove:function(a){var d=a.target.nodeName.toLowerCase();if("td"===d||"th"===d)this._drawSelection(a.target,a),this._shiftScroll(a)},_mouseup:function(a){c(g.body).off(".autoFill");
var d=this,b=this.s.dt,e=this.dom.select;e.top.remove();e.left.remove();e.right.remove();e.bottom.remove();this.dom.handle.css("display","block");e=this.s.start;var f=this.s.end;if(e.row!==f.row||e.column!==f.column){var m=b.cell(":eq("+e.row+")",e.column+":visible",{page:"current"});if(c("div.DTE",m.node()).length){var n=b.editor();n.on("submitSuccess.dtaf close.dtaf",function(){n.off(".dtaf");setTimeout(function(){d._mouseup(a)},100)}).on("submitComplete.dtaf preSubmitCancelled.dtaf close.dtaf",
function(){n.off(".dtaf")});n.submit()}else{var p=this._range(e.row,f.row);e=this._range(e.column,f.column);f=[];for(var q=b.settings()[0],v=q.aoColumns,u=b.columns(this.c.columns).indexes(),w=0;w<p.length;w++)f.push(c.map(e,function(t){var x=b.row(":eq("+p[w]+")",{page:"current"});t=b.cell(x.index(),t+":visible");x=t.data();var z=t.index(),A=v[z.column].editField;A!==k&&(x=q.oApi._fnGetObjectDataFn(A)(b.row(z.row).data()));if(-1!==u.indexOf(z.column))return{cell:t,data:x,label:t.data(),index:z}}));
this._actionSelector(f);clearInterval(this.s.scrollInterval);this.s.scrollInterval=null}}},_range:function(a,d){var b=[];if(a<=d)for(;a<=d;a++)b.push(a);else for(;a>=d;a--)b.push(a);return b},_shiftScroll:function(a){var d=this,b=this.s.scroll,e=!1,f=a.pageY-g.body.scrollTop,m=a.pageX-g.body.scrollLeft,n,p,q,v;65>f?n=-5:f>b.windowHeight-65&&(n=5);65>m?p=-5:m>b.windowWidth-65&&(p=5);null!==b.dtTop&&a.pageY<b.dtTop+65?q=-5:null!==b.dtTop&&a.pageY>b.dtTop+b.dtHeight-65&&(q=5);null!==b.dtLeft&&a.pageX<
b.dtLeft+65?v=-5:null!==b.dtLeft&&a.pageX>b.dtLeft+b.dtWidth-65&&(v=5);n||p||q||v?(b.windowVert=n,b.windowHoriz=p,b.dtVert=q,b.dtHoriz=v,e=!0):this.s.scrollInterval&&(clearInterval(this.s.scrollInterval),this.s.scrollInterval=null);!this.s.scrollInterval&&e&&(this.s.scrollInterval=setInterval(function(){b.windowVert&&(g.body.scrollTop+=b.windowVert);b.windowHoriz&&(g.body.scrollLeft+=b.windowHoriz);if(b.dtVert||b.dtHoriz){var u=d.dom.dtScroll[0];b.dtVert&&(u.scrollTop+=b.dtVert);b.dtHoriz&&(u.scrollLeft+=
b.dtHoriz)}},20))},_update:function(a,d){if(!1!==a){a=this.s.dt;var b=a.columns(this.c.columns).indexes();this._emitEvent("preAutoFill",[a,d]);this._editor(d);if(null!==this.c.update?this.c.update:!this.c.editor){for(var e=0,f=d.length;e<f;e++)for(var m=0,n=d[e].length;m<n;m++){var p=d[e][m];-1!==b.indexOf(p.index.column)&&p.cell.data(p.set)}a.draw(!1)}this._emitEvent("autoFill",[a,d])}}});r.actions={increment:{available:function(a,d){a=d[0][0].label;return!isNaN(a-parseFloat(a))},option:function(a,
d){return a.i18n("autoFill.increment",'Increment / decrement each cell by: <input type="number" value="1">')},execute:function(a,d,b){a=1*d[0][0].data;b=1*c("input",b).val();for(var e=0,f=d.length;e<f;e++)for(var m=0,n=d[e].length;m<n;m++)d[e][m].set=a,a+=b}},fill:{available:function(a,d){return!0},option:function(a,d){return a.i18n("autoFill.fill","Fill all cells with <i>%d</i>",d[0][0].label)},execute:function(a,d,b){a=d[0][0].data;b=0;for(var e=d.length;b<e;b++)for(var f=0,m=d[b].length;f<m;f++)d[b][f].set=
a}},fillHorizontal:{available:function(a,d){return 1<d.length&&1<d[0].length},option:function(a,d){return a.i18n("autoFill.fillHorizontal","Fill cells horizontally")},execute:function(a,d,b){a=0;for(b=d.length;a<b;a++)for(var e=0,f=d[a].length;e<f;e++)d[a][e].set=d[a][0].data}},fillVertical:{available:function(a,d){return 1<d.length},option:function(a,d){return a.i18n("autoFill.fillVertical","Fill cells vertically")},execute:function(a,d,b){a=0;for(b=d.length;a<b;a++)for(var e=0,f=d[a].length;e<f;e++)d[a][e].set=
d[0][e].data}},cancel:{available:function(){return!1},option:function(a){return a.i18n("autoFill.cancel","Cancel")},execute:function(){return!1}}};r.version="2.3.9";r.defaults={alwaysAsk:!1,focus:null,columns:"",enable:!0,update:null,editor:null,vertical:!0,horizontal:!0};r.classes={btn:"btn"};var B=c.fn.dataTable.Api;B.register("autoFill()",function(){return this});B.register("autoFill().enabled()",function(){var a=this.context[0];return a.autoFill?a.autoFill.enabled():!1});B.register("autoFill().enable()",
function(a){return this.iterator("table",function(d){d.autoFill&&d.autoFill.enable(a)})});B.register("autoFill().disable()",function(){return this.iterator("table",function(a){a.autoFill&&a.autoFill.disable()})});c(g).on("preInit.dt.autofill",function(a,d,b){"dt"===a.namespace&&(a=d.oInit.autoFill,b=l.defaults.autoFill,a||b)&&(b=c.extend({},a,b),!1!==a&&new r(d,b))});l.AutoFill=r;return l.AutoFill=r});
