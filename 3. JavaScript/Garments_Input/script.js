window.onbeforeunload = function() {
    return "Dude, are you sure you want to leave? Think of the kittens!";
}

function addGarmentFromAbove()
{
    var rc = 1;
    var no = getNo();
    var name = document.getElementById('name');
    var reg = document.getElementById("reg");
    var hat = document.getElementById("hat");
    var shoulder = document.getElementById("shoulder");
    var sleeve = document.getElementById("sleeve");
    var back = document.getElementById("back");
    var center_back = document.getElementById("center_back");
    var up_length = document.getElementById("up_length");
    var collar = document.getElementById("collar");
    var chest = document.getElementById("chest");
    var up_waist = document.getElementById("up_waist");
    var up_bottom = document.getElementById("up_bottom");
    var dw_waist = document.getElementById("dw_waist");
    var dw_bottom = document.getElementById("dw_bottom");
    var crotch = document.getElementById("crotch");
    var ft_crotch = document.getElementById("ft_crotch");
    var thigh = document.getElementById("thigh");
    var dw_len = document.getElementById("dw_len");
    var skirt_len = document.getElementById("skirt_len");
    var remark = document.getElementById("remark");

    rc = validation(name.value);

    if (0 == rc)
    {
        return;
    }
    else
    {   
        appendTableRowFromAbove(no, name, reg, hat, shoulder, sleeve, back, center_back, up_length, collar, chest, up_waist, up_bottom, dw_waist, dw_bottom, crotch, ft_crotch, thigh, dw_len, skirt_len, remark);
        return;
    }
}

function appendTableRowFromAbove(no, name, reg, hat, shoulder, sleeve, back, center_back, up_length, collar, chest, up_waist, up_bottom, dw_waist, dw_bottom, crotch, ft_crotch, thigh, dw_len, skirt_len, remark)
{
    // alert('sequence1');
    var rowId = 'row' + no;
    var val_no = document.createTextNode(no);
    var val_name = document.createTextNode(name.value);
    var val_reg = document.createTextNode(reg.value);
    var val_hat = document.createTextNode(hat.value);
    var val_shoulder = document.createTextNode(shoulder.value);
    var val_sleeve = document.createTextNode(sleeve.value);
    var val_back = document.createTextNode(back.value);
    var val_center_back = document.createTextNode(center_back.value);
    var val_up_length = document.createTextNode(up_length.value);
    var val_collar = document.createTextNode(collar.value);
    var val_chest = document.createTextNode(chest.value);
    var val_up_waist = document.createTextNode(up_waist.value);
    var val_up_bottom = document.createTextNode(up_bottom.value);
    var val_dw_waist = document.createTextNode(dw_waist.value);
    var val_dw_bottom = document.createTextNode(dw_bottom.value);
    var val_crotch = document.createTextNode(crotch.value);
    var val_ft_crotch = document.createTextNode(ft_crotch.value);
    var val_thigh = document.createTextNode(thigh.value);
    var val_dw_len = document.createTextNode(dw_len.value);
    var val_skirt_len = document.createTextNode(skirt_len.value);
    var val_remark = document.createTextNode(remark.value);
     
    var tbody = document.getElementById("tbody");
    var new_tr = document.createElement('tr');
    new_tr.setAttribute("id", rowId);
    
    var span_no = document.createElement('span')
    var td_no = document.createElement('td');
    span_no.appendChild(val_no);
    td_no.appendChild(span_no);
    new_tr.appendChild(td_no);

    var span_reg = document.createElement('span')
    var td_reg = document.createElement('td');
    span_reg.appendChild(val_reg);
    span_reg.setAttribute('id',reg.value);
    td_reg.appendChild(span_reg);
    new_tr.appendChild(td_reg);

    var span_name = document.createElement('span')
    var td_name = document.createElement('td');
    span_name.appendChild(val_name);
    span_name.setAttribute('id',name.value);
    td_name.appendChild(span_name);
    new_tr.appendChild(td_name);

    var span_hat = document.createElement('span')
    var td_hat = document.createElement('td');
    span_hat.appendChild(val_hat);
    td_hat.appendChild(span_hat);
    new_tr.appendChild(td_hat);

    var span_shoulder = document.createElement('span')
    var td_shoulder = document.createElement('td');
    span_shoulder.appendChild(val_shoulder);
    td_shoulder.appendChild(span_shoulder);
    new_tr.appendChild(td_shoulder);

    var span_sleeve = document.createElement('span')
    var td_sleeve = document.createElement('td');
    span_sleeve.appendChild(val_sleeve);
    td_sleeve.appendChild(span_sleeve);
    new_tr.appendChild(td_sleeve);

    var span_back = document.createElement('span')
    var td_back = document.createElement('td');
    span_back.appendChild(val_back);
    td_back.appendChild(span_back);
    new_tr.appendChild(td_back);

    var span_center_back = document.createElement('span')
    var td_center_back = document.createElement('td');
    span_center_back.appendChild(val_center_back);
    td_center_back.appendChild(span_center_back);
    new_tr.appendChild(td_center_back);

    var span_up_length = document.createElement('span')
    var td_up_length = document.createElement('td');
    span_up_length.appendChild(val_up_length);
    td_up_length.appendChild(span_up_length);
    new_tr.appendChild(td_up_length);

    var span_collar = document.createElement('span')
    var td_collar = document.createElement('td');
    span_collar.appendChild(val_collar);
    td_collar.appendChild(span_collar);
    new_tr.appendChild(td_collar);

    var span_chest = document.createElement('span')
    var td_chest = document.createElement('td');
    span_chest.appendChild(val_chest);
    td_chest.appendChild(span_chest);
    new_tr.appendChild(td_chest);

    var span_up_waist = document.createElement('span')
    var td_up_waist = document.createElement('td');
    span_up_waist.appendChild(val_up_waist);
    td_up_waist.appendChild(span_up_waist);
    new_tr.appendChild(td_up_waist);

    var span_up_bottom = document.createElement('span')
    var td_up_bottom = document.createElement('td');
    span_up_bottom.appendChild(val_up_bottom);
    td_up_bottom.appendChild(span_up_bottom);
    new_tr.appendChild(td_up_bottom);

    var span_dw_waist = document.createElement('span')
    var td_dw_waist = document.createElement('td');
    span_dw_waist.appendChild(val_dw_waist);
    td_dw_waist.appendChild(span_dw_waist);
    new_tr.appendChild(td_dw_waist);

    var span_dw_bottom = document.createElement('span')
    var td_dw_bottom = document.createElement('td');
    span_dw_bottom.appendChild(val_dw_bottom);
    td_dw_bottom.appendChild(span_dw_bottom);
    new_tr.appendChild(td_dw_bottom);

    var span_crotch = document.createElement('span')
    var td_crotch = document.createElement('td');
    span_crotch.appendChild(val_crotch);
    td_crotch.appendChild(span_crotch);
    new_tr.appendChild(td_crotch);

    var span_ft_crotch = document.createElement('span')
    var td_ft_crotch = document.createElement('td');
    span_ft_crotch.appendChild(val_ft_crotch);
    td_ft_crotch.appendChild(span_ft_crotch);
    new_tr.appendChild(td_ft_crotch);

    var span_thigh = document.createElement('span')
    var td_thigh = document.createElement('td');
    span_thigh.appendChild(val_thigh);
    td_thigh.appendChild(span_thigh);
    new_tr.appendChild(td_thigh);

    var span_dw_len = document.createElement('span')
    var td_dw_len = document.createElement('td');
    span_dw_len.appendChild(val_dw_len);
    td_dw_len.appendChild(span_dw_len);
    new_tr.appendChild(td_dw_len);

    var span_skirt_len = document.createElement('span')
    var td_skirt_len = document.createElement('td');
    span_skirt_len.appendChild(val_skirt_len);
    td_skirt_len.appendChild(span_skirt_len);
    new_tr.appendChild(td_skirt_len);

    var span_remark = document.createElement('span')
    var td_remark = document.createElement('td');
    span_remark.appendChild(val_remark);
    td_remark.appendChild(span_remark);
    new_tr.appendChild(td_remark);

    var val_button_rm = document.createTextNode("刪 除");
    var button_rm = document.createElement('button')
    var td_rm = document.createElement('td');
    button_rm.setAttribute("id", rowId);
    button_rm.setAttribute("onclick", "deleteTableRow(this.id)");
    button_rm.appendChild(val_button_rm);
    td_rm.appendChild(button_rm);
    new_tr.appendChild(td_rm);

    var form = document.createElement('form');

    var val_button_amd = document.createTextNode("修 改");
    var button_amd = document.createElement('button')
    var td_amd = document.createElement('td');
    button_amd.setAttribute("id", rowId);
    button_amd.setAttribute("type", "reset");
    button_amd.setAttribute("onclick", "amendById(this.id)");
    button_amd.appendChild(val_button_amd);
   
    var col_id = "col_of_" + rowId;
    var col_val = document.createElement('input');   
    col_val.setAttribute('id',col_id);
    col_val.setAttribute('type','text');
    col_val.setAttribute('size','1'); 

    var val_id = "val_of_col_" + rowId;
    var input_val = document.createElement('input');
    input_val.setAttribute('id',val_id);
    input_val.setAttribute('type','text');
    input_val.setAttribute('size','5');
        
    form.appendChild(button_amd);
    form.appendChild(col_val);
    form.appendChild(input_val);

    td_amd.appendChild(form);
    new_tr.appendChild(td_amd);
    
    tbody.insertBefore(new_tr, tbody.childNodes[0]);
    // tbody.appendChild(new_tr);
    return;
}

function addGarmentFromBehind()
{
    var rc = 1;
    var no = getNo();
    var name = document.getElementById('name');
    var reg = document.getElementById("reg");
    var hat = document.getElementById("hat");
    var shoulder = document.getElementById("shoulder");
    var sleeve = document.getElementById("sleeve");
    var back = document.getElementById("back");
    var center_back = document.getElementById("center_back");
    var up_length = document.getElementById("up_length");
    var collar = document.getElementById("collar");
    var chest = document.getElementById("chest");
    var up_waist = document.getElementById("up_waist");
    var up_bottom = document.getElementById("up_bottom");
    var dw_waist = document.getElementById("dw_waist");
    var dw_bottom = document.getElementById("dw_bottom");
    var crotch = document.getElementById("crotch");
    var ft_crotch = document.getElementById("ft_crotch");
    var thigh = document.getElementById("thigh");
    var dw_len = document.getElementById("dw_len");
    var skirt_len = document.getElementById("skirt_len");
    var remark = document.getElementById("remark");

    rc = validation(name.value);

    if (0 == rc)
    {
        return;
    }
    else
    {   
        appendTableRowFromBehind(no, name, reg, hat, shoulder, sleeve, back, center_back, up_length, collar, chest, up_waist, up_bottom, dw_waist, dw_bottom, crotch, ft_crotch, thigh, dw_len, skirt_len, remark);
        return;
    }
}

function appendTableRowFromBehind(no, name, reg, hat, shoulder, sleeve, back, center_back, up_length, collar, chest, up_waist, up_bottom, dw_waist, dw_bottom, crotch, ft_crotch, thigh, dw_len, skirt_len, remark)
{
    // alert('sequence1');
    var rowId = 'row' + no;
    var val_no = document.createTextNode(no);
    var val_name = document.createTextNode(name.value);
    var val_reg = document.createTextNode(reg.value);
    var val_hat = document.createTextNode(hat.value);
    var val_shoulder = document.createTextNode(shoulder.value);
    var val_sleeve = document.createTextNode(sleeve.value);
    var val_back = document.createTextNode(back.value);
    var val_center_back = document.createTextNode(center_back.value);
    var val_up_length = document.createTextNode(up_length.value);
    var val_collar = document.createTextNode(collar.value);
    var val_chest = document.createTextNode(chest.value);
    var val_up_waist = document.createTextNode(up_waist.value);
    var val_up_bottom = document.createTextNode(up_bottom.value);
    var val_dw_waist = document.createTextNode(dw_waist.value);
    var val_dw_bottom = document.createTextNode(dw_bottom.value);
    var val_crotch = document.createTextNode(crotch.value);
    var val_ft_crotch = document.createTextNode(ft_crotch.value);
    var val_thigh = document.createTextNode(thigh.value);
    var val_dw_len = document.createTextNode(dw_len.value);
    var val_skirt_len = document.createTextNode(skirt_len.value);
    var val_remark = document.createTextNode(remark.value);
        
    var tbody = document.getElementById("tbody");
    var new_tr = document.createElement('tr');
    new_tr.setAttribute("id", rowId);
    
    var span_no = document.createElement('span')
    var td_no = document.createElement('td');
    span_no.appendChild(val_no);
    td_no.appendChild(span_no);
    new_tr.appendChild(td_no);

    var span_reg = document.createElement('span')
    var td_reg = document.createElement('td');
    span_reg.appendChild(val_reg);
    span_reg.setAttribute('id',reg.value);
    td_reg.appendChild(span_reg);
    new_tr.appendChild(td_reg);

    var span_name = document.createElement('span')
    var td_name = document.createElement('td');
    span_name.appendChild(val_name);
    span_name.setAttribute('id',name.value);
    td_name.appendChild(span_name);
    new_tr.appendChild(td_name);

    var span_hat = document.createElement('span')
    var td_hat = document.createElement('td');
    span_hat.appendChild(val_hat);
    td_hat.appendChild(span_hat);
    new_tr.appendChild(td_hat);

    var span_shoulder = document.createElement('span')
    var td_shoulder = document.createElement('td');
    span_shoulder.appendChild(val_shoulder);
    td_shoulder.appendChild(span_shoulder);
    new_tr.appendChild(td_shoulder);

    var span_sleeve = document.createElement('span')
    var td_sleeve = document.createElement('td');
    span_sleeve.appendChild(val_sleeve);
    td_sleeve.appendChild(span_sleeve);
    new_tr.appendChild(td_sleeve);

    var span_back = document.createElement('span')
    var td_back = document.createElement('td');
    span_back.appendChild(val_back);
    td_back.appendChild(span_back);
    new_tr.appendChild(td_back);

    var span_center_back = document.createElement('span')
    var td_center_back = document.createElement('td');
    span_center_back.appendChild(val_center_back);
    td_center_back.appendChild(span_center_back);
    new_tr.appendChild(td_center_back);

    var span_up_length = document.createElement('span')
    var td_up_length = document.createElement('td');
    span_up_length.appendChild(val_up_length);
    td_up_length.appendChild(span_up_length);
    new_tr.appendChild(td_up_length);

    var span_collar = document.createElement('span')
    var td_collar = document.createElement('td');
    span_collar.appendChild(val_collar);
    td_collar.appendChild(span_collar);
    new_tr.appendChild(td_collar);

    var span_chest = document.createElement('span')
    var td_chest = document.createElement('td');
    span_chest.appendChild(val_chest);
    td_chest.appendChild(span_chest);
    new_tr.appendChild(td_chest);

    var span_up_waist = document.createElement('span')
    var td_up_waist = document.createElement('td');
    span_up_waist.appendChild(val_up_waist);
    td_up_waist.appendChild(span_up_waist);
    new_tr.appendChild(td_up_waist);

    var span_up_bottom = document.createElement('span')
    var td_up_bottom = document.createElement('td');
    span_up_bottom.appendChild(val_up_bottom);
    td_up_bottom.appendChild(span_up_bottom);
    new_tr.appendChild(td_up_bottom);

    var span_dw_waist = document.createElement('span')
    var td_dw_waist = document.createElement('td');
    span_dw_waist.appendChild(val_dw_waist);
    td_dw_waist.appendChild(span_dw_waist);
    new_tr.appendChild(td_dw_waist);

    var span_dw_bottom = document.createElement('span')
    var td_dw_bottom = document.createElement('td');
    span_dw_bottom.appendChild(val_dw_bottom);
    td_dw_bottom.appendChild(span_dw_bottom);
    new_tr.appendChild(td_dw_bottom);

    var span_crotch = document.createElement('span')
    var td_crotch = document.createElement('td');
    span_crotch.appendChild(val_crotch);
    td_crotch.appendChild(span_crotch);
    new_tr.appendChild(td_crotch);

    var span_ft_crotch = document.createElement('span')
    var td_ft_crotch = document.createElement('td');
    span_ft_crotch.appendChild(val_ft_crotch);
    td_ft_crotch.appendChild(span_ft_crotch);
    new_tr.appendChild(td_ft_crotch);

    var span_thigh = document.createElement('span')
    var td_thigh = document.createElement('td');
    span_thigh.appendChild(val_thigh);
    td_thigh.appendChild(span_thigh);
    new_tr.appendChild(td_thigh);

    var span_dw_len = document.createElement('span')
    var td_dw_len = document.createElement('td');
    span_dw_len.appendChild(val_dw_len);
    td_dw_len.appendChild(span_dw_len);
    new_tr.appendChild(td_dw_len);

    var span_skirt_len = document.createElement('span')
    var td_skirt_len = document.createElement('td');
    span_skirt_len.appendChild(val_skirt_len);
    td_skirt_len.appendChild(span_skirt_len);
    new_tr.appendChild(td_skirt_len);

    var span_remark = document.createElement('span')
    var td_remark = document.createElement('td');
    span_remark.appendChild(val_remark);
    td_remark.appendChild(span_remark);
    new_tr.appendChild(td_remark);

    var val_button_rm = document.createTextNode("刪 除");
    var button_rm = document.createElement('button')
    var td_rm = document.createElement('td');
    button_rm.setAttribute("id", rowId);
    button_rm.setAttribute("onclick", "deleteTableRow(this.id)");
    button_rm.appendChild(val_button_rm);
    td_rm.appendChild(button_rm);
    new_tr.appendChild(td_rm);

    var form = document.createElement('form');

    var val_button_amd = document.createTextNode("修 改");
    var button_amd = document.createElement('button')
    var td_amd = document.createElement('td');
    button_amd.setAttribute("id", rowId);
    button_amd.setAttribute("type", "reset");
    button_amd.setAttribute("onclick", "amendById(this.id)");
    button_amd.appendChild(val_button_amd);
    
    var col_id = "col_of_" + rowId;
    var col_val = document.createElement('input');   
    col_val.setAttribute('id',col_id);
    col_val.setAttribute('type','text');
    col_val.setAttribute('size','1'); 

    var val_id = "val_of_col_" + rowId;
    var input_val = document.createElement('input');
    input_val.setAttribute('id',val_id);
    input_val.setAttribute('type','text');
    input_val.setAttribute('size','2');
        
    form.appendChild(button_amd);
    form.appendChild(col_val);
    form.appendChild(input_val);

    td_amd.appendChild(form);
    new_tr.appendChild(td_amd);

    // tbody.insertBefore(new_tr, tbody.childNodes[0]);
    tbody.appendChild(new_tr);
    return;
}

function deleteTableRow(id)
{
    alert('刪 除 '+ id + '列 嗎?');
    document.getElementById(id).remove();
    return;
}

function amendById(id)
{
    var col_id = "col_of_" + id;
    var val_id = "val_of_col_" + id;
    var col_of = document.getElementById(col_id);
    var val_of_col = document.getElementById(val_id);
    var num = col_of.value;
    var amd_txt = val_of_col.value;

    parseInt(num);

    var row = document.getElementById(id).childNodes;
    row[num-1].innerText = amd_txt;

    return;
}

function search()
{
    var name = document.getElementById('name');
    var reg = document.getElementById("reg");
    var txt_name = name.value;
    var txt_reg = reg.value;

    if ("" != txt_name)
    {
        var name_found = document.getElementById(txt_name);
        name_found.style.backgroundColor ="yellow";
    }

    if ("" != txt_reg)
    {
        var reg_found =  document.getElementById(txt_reg);
        reg_found.style.backgroundColor ="yellow";
    }
    return;
}

/* Side Functions */
function validation(chk)
{
    if ("" == chk)
    {
        alert('請輸入人名');
        return 0;
    } 
}

function getNo()
{
    var table = document.getElementById('displayTable');
    var tbodyRowCount = table.tBodies[0].rows.length;
    return tbodyRowCount+1;
}