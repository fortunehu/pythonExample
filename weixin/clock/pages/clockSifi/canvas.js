const ctx = wx.createCanvasContext('firstCanvas');
var windowWidth;
var windowHeight;
var radius;
var sNums = 8;

var turnWheel = {
  rewardNames: [],				//转盘奖品名称数组
  colors: []				//转盘奖品区块对应背景颜色
};

turnWheel.rewardNames = [
  "黄焖鸡", "小胖",
  "TTT", "Word餐",
  "沙县", "武大食堂",
  "谢谢参与", "Today"];

turnWheel.colors = [
  "#EF2A31", "#EF4B30",
  "#F88824", "#FFBD11",
  "#FBF200", "#68BB45",
  "#00A654", "#1182C6"];

function degToRad(degree) {
    var factor = Math.PI / 180;
    return degree * factor;
}

var timer;

var dStartV = Math.PI*0.5;
var dAccelV = Math.PI*0.23;
var dStartDeg = 0;
var dTime = 0.0;
var dTimeTotal = 15.0;
var curDeg = 0;
var dStartDegLast = 0;

var bRotate = false;

// Define how to draw the Hands
function drawHand(ctx, centerX, centerY, radius, ang, width, color) {

  ctx.save();
  ctx.beginPath();
  ctx.setLineWidth(width);
  ctx.setLineCap('round');
  ctx.moveTo(centerX, centerY);
  var dx, dy;
  dx = centerX + Math.cos(ang)*radius;
  dy = centerY + Math.sin(ang)*radius;

  ctx.lineTo(dx, dy);
  ctx.setStrokeStyle(color);
  ctx.stroke();

  ctx.restore();
}

function renderTime() {

    /** background fill*/
    var ang;
    var deltaAng;

    var centerX, centerY;
    centerX = windowWidth * 0.5;
    centerY = windowHeight * 0.5;
    var nNums = sNums;

    deltaAng = 2.0 * Math.PI / nNums;
    var curClr;
    var curDegOffset;
 
    if (dTime < dTimeTotal && bRotate)
    {
        dTime += 1;
        curDegOffset = (dStartV * dTime - 0.5 * dAccelV * dTime * dTime);
        if (curDegOffset > 0)
          dStartDeg += curDegOffset;
        else 
          bRotate = false;
    }
    else 
      bRotate = false;
    
    // Define the text styles
    ctx.setFontSize(14);
    //ctx.setFillStyle("#000000");
    // ctx.textBaseline = "middle";
    ctx.setTextAlign('center');

    // Rotate and put number and rotate back
    for (var num = 0; num < nNums; num++) {
      ang =   dStartDeg + num * deltaAng;
      ///
      ctx.save();
      curClr = turnWheel.colors[num];
      ctx.setFillStyle(curClr)

      ctx.beginPath();
      ctx.moveTo(centerX, centerY);
      ctx.arc(centerX, centerY, radius, ang, ang + deltaAng);
      //ctx.setFillStyle(sColorList.indexOf[num]);
      ctx.fill();
      ctx.restore();
    }
    ctx.restore();

    //
    drawHand(ctx, centerX, centerY, radius * 0.8, 1.5*Math.PI, 4, "#CACACA")
    /** hand end**/
    ctx.draw(true);
}


Page({
    canvasIdErrorCallback: function(e) {
        console.error(e.detail.errMsg)
    },
    bindbt: function () {
      if (bRotate)
        return;

      dTime = 0.0;
      bRotate = true;

      // if (dStartDeg >= 2 * Math.PI)
      //   dStartDeg %= 2 * Math.PI;
    },
    onReady: function(e) {
        wx.getSystemInfo({
            success: function(res) {
                windowWidth = res.windowWidth;
                windowHeight = res.windowHeight;
                radius = (windowWidth - 20) / 2;

                var nNums = sNums;
                for (var iClr = 0; iClr < nNums; iClr++) {
                  sColorList.push(getRandomColor())
                }
                
            }
        });
    },

    onShow: function (e) {
      wx.getSystemInfo({
        success: function (res) {
          // Center the ctx
          // Draw the Clock every second
          timer = setInterval(renderTime, 100);
        }
      });
    },
    onHide: function (e) {
      ctx.clearRect(0, 0, windowWidth, windowHeight)
      clearInterval(timer);
    }
})