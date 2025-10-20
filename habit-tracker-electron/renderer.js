const { ipcRenderer } = require('electron');

// 提交评分
document.getElementById('habit-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  const habit = document.getElementById('habit').value;
  const score = parseInt(document.getElementById('score').value, 10);
  const date = new Date().toISOString().split('T')[0];

  try {
    await ipcRenderer.invoke('insert-record', { date, habit, score });
    alert('评分提交成功！');
    loadRecords();
  } catch (err) {
    alert(`提交失败：${err}`);
  }
});

// 加载评分记录
async function loadRecords() {
  try {
    const records = await ipcRenderer.invoke('fetch-records');
    const tableBody = document.querySelector('#records-table tbody');
    tableBody.innerHTML = '';
    records.forEach((record) => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${record.date}</td>
        <td>${record.habit}</td>
        <td>${record.score}</td>
      `;
      tableBody.appendChild(row);
    });
  } catch (err) {
    alert(`加载记录失败：${err}`);
  }
}

// 初始化加载
loadRecords();