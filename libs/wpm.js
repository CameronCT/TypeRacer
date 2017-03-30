
/*
!wpm 23 24 25 23 25 26 49

!wpm 40, 101, 37, 76, 39, 74, 42, 66, 41, 31, 60, 26, 65, 109, 70, 94, 15, 129, 43, 82, 27, 91, 65, 48, 97, 62, 47, 19, 33, 70, 41, 104, 45, 61, 68, 81, 66, 35, 57, 54, 62, 55, 83, 39, 19, 82, 59, 93, 26, 60, 54, 63, 66, 41, 40, 26, 91, 36, 62, 20, 102, 77, 47, 23, 50, 55, 41, 18, 153, 66, 87, 73, 89, 28, 70, 29, 80, 17, 80, 76, 37, 33, 78, 39, 24, 104, 19, 23, 39, 25, 78, 94, 23, 50, 72, 56, 32, 89, 36, 43, 60, 41, 72, 54, 23, 78, 22, 66, 23, 24, 80, 49, 48, 29, 72, 44, 86, 68, 62, 49, 66, 39, 109, 73, 56, 65, 76, 72, 41, 65, 68, 28, 47, 27, 64, 37, 23, 9, 69, 43, 60, 34, 68, 73, 29, 62, 44, 56, 15, 95, 10, 84, 14, 65, 29, 32, 40, 109, 27, 18, 25, 51, 46, 69, 39, 32, 62, 44, 60, 78, 30, 27, 89, 38, 75, 67, 74, 18, 48, 51, 53, 60, 21, 44

!wpm 40, 101, 37, 76, 39, 74, 42, 66, 41, 31, 60, 26, 65, 109, 70, 94, 15, 129, 43, 82, 27, 91, 65, 48, 97, 62, 47, 19, 33, 70, 41, 104, 45, 61, 68, 81, 66, 35, 57, 54, 62, 55, 83, 39, 19, 82, 59, 93, 26, 60, 54, 63, 66, 41, 40, 26, 91, 36, 62, 20, 102, 77, 47, 23, 50, 55, 41, 18, 153, 66, 87, 73, 89, 28, 70, 29, 80, 17, 80, 76, 37, 33, 78, 39, 24, 104, 19, 23, 39, 25, 78, 94, 23, 50, 72, 56, 32, 89, 36, 43, 60, 41, 72, 54, 23, 78, 22, 66, 23, 24, 80, 49, 48, 29, 72, 44, 86, 68, 62, 49, 66, 39, 109, 73, 56, 65, 76, 72, 41, 65, 68, 28, 47, 27, 64, 37, 23, 9, 69, 43, 60, 34, 68, 73, 29, 62, 44,  56, 15, 95, 10, 84, 14, 65, 29, 32, 40, 109, 27, 18, 25, 51, 46, 69, 39
*/

module.exports = {

    process: function(data) {
        //var data = document.getElementById('data').value;
        
        data = data.replace(/^(\d(?!__))+/, '');
        data = data.replace(/\D+$/, '');
        data = data.replace(/\n/g, '');
        
        var times = [];
        var total_time = 0;
        var typed_chars = '';
        var formatted_chars = [];
        
        var re = /((\D|\d__)+)((\d(?!__))+)/g;
        var m;
        
        while (m = re.exec(data)) {
            var letter = m[1];
            typed_chars += String(letter.charAt(0)).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
            
            letter = letter.replace(/(\d)__/g, '$1');
            letter = letter.replace(/(.)(.+)/, function(match, g1, g2) {
                return g1 + String(g2).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
            });
            letter = letter.replace(/./, function(c) {
                if (c == ' ') c = '_';
                return '**' + String(c).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); + '**';
            });
            
            formatted_chars.push(letter);
            
            var time = Number(m[3]);
            times.push([time, 0]);
            total_time += time;
        }
        
        var num_chars = times.length;
        if (!num_chars) {
            return '<SYNTAX> !wpm <data>';
        }
        
        
        for (var i = 0; i < num_chars; i++) {
            if (times[i][0] < 20) times[i][1] = 1;
            
            if (i > num_chars-10) continue;
            
            var min, max;
            min = max = times[i][0];
            for (var j = i+1; j < i+10; j++) {
                min = Math.min(min, times[j][0]);
                max = Math.max(max, times[j][0]);
            }
            if (max-min <= 10) {
                for (var j = i; j < i+10; j++) {
                    times[j][1] = 1;
                }
            }
        }

        var formatted_times = times.map(function(time) {
		if (time[1]) return '<span class="highlight">' + time[0] + '</span>';
            return time[0];
        });
        
        var formatted_log = '';
        
        for (var i = 0; i < num_chars; i++) {
            if (times[i][1]) {
                formatted_log += '**';
            }
            else {
                formatted_log += '*';
            }
            
            formatted_log += times[i][0] + '**' + ' ' + formatted_chars[i] + ' ';
        }
        
        var res = '';

        res += "*\"" + typed_chars + "\"*\n\n";
        res += "**Total Typed Characters (including typos):** \n    " + num_chars + "\n\n";
        res += "**Time:** \n    " + total_time/1000 + " seconds\n\n";
        res += "**WPM (Assumed 100% Accuracy):** \n    " + (num_chars/total_time*1000*60/5).toFixed(2) + " WPM\n\n";
        res += "If you want more statistics, please visit: https://jsfiddle.net/canissimia/9z8qcta7/";
        return res;
    }

}
