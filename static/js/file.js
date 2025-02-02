
function toggleFolder(element) {
  element.classList.toggle('open');
}



function displayFileContent() {
  const modal = document.getElementById("file-content-modal");
  modal.style.display = "block";
}


function closeModal() {
  const modal = document.getElementById("file-content-modal");
  modal.style.display = "none";
}

function uploadfile(){
    const modal = document.getElementById("upload-form");
    var formData = new FormData(modal);
    var xhr = new XMLHttpRequest();
     xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        // 上传成功，更新消息容器的内容
          alert("上传成功");
          closeModal();
           document.getElementById('content').innerHTML = xhr.responseText;
      } else {
        // 上传失败，显示错误消息
        document.getElementById("upload-message").textContent = "文件上传失败！";
      }
    }
  };

  xhr.open("POST", "/upload");
  xhr.send(formData);

}
function viewRow(index){
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        var rowData = JSON.parse(xhr.responseText);
         const fileTable = document.getElementById("data_file");
        const tbody = fileTable.querySelector("tbody");
        tbody.innerHTML = "";
        rowData.forEach(file => {
      const row = document.createElement("tr");
      const filenameCell = document.createElement("td");
      filenameCell.textContent = file.title;
      const contentCell = document.createElement("td");
      contentCell.textContent = file.content;
      row.appendChild(filenameCell);
      row.appendChild(contentCell);
      tbody.appendChild(row);
    });

          showModal();
        console.log("查看行数据:", rowData);
      } else {
        console.error("查看行数据失败");
      }
    }
  };

  xhr.open("GET", "/view?index=" + index);
  xhr.send();
}

function deleteRow(index){
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
         document.getElementById('content').innerHTML = xhr.responseText;
        console.log("删除行数据成功");
        // 刷新表格或其他操作
      } else {
        console.error("删除行数据失败");
      }
    }
  };

  xhr.open("POST", "/delete");
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhr.send("index=" + index);
}


function excuteRow(index,button){
    button.classList.add('loading');
    button.disabled = true;
 var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        console.log("执行行数据成功");
        alert("生成完成，请重新刷新页面，查看详细视频路径");
        // 刷新表格或其他操作
      } else {
        console.error("执行行数据失败");
      }
    }
  };
   xhr.open("GET", "/batch?index=" + index);
  xhr.send();
}

function showModal() {
        const modal = document.getElementById("dataModal");
        modal.style.display = "block";
        alert(modal);

    }
 function   closeModal_data(){
 const modal = document.getElementById("dataModal");
     modal.style.display = "none";
 }