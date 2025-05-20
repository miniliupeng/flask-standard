// 等待DOM加载完成
document.addEventListener('DOMContentLoaded', function() {
    console.log('应用已加载');
    
    // 闪现消息自动关闭
    const flashes = document.querySelectorAll('.flash');
    flashes.forEach(flash => {
        setTimeout(() => {
            flash.style.opacity = '0';
            flash.style.transition = 'opacity 0.5s';
            setTimeout(() => {
                flash.remove();
            }, 500);
        }, 3000);
    });
}); 