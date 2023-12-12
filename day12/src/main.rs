
use std::thread;
use std::sync::{mpsc, Arc, Mutex};

fn verify_line(line: &str, expected: &[usize]) -> bool {
    let mut b = 0;
    let mut b_set = 0;
    let mut b_count :usize = 0;

    for (idx, char) in line.chars().enumerate() {
        if b_set >= expected.len() {
            if !line[idx..].contains('#') {
                return true;
            } else {
                return false;
            }
        }

        if char == '#' {
            b += 1;
            b_count += 1;
        } else {
            if b > 0 {
                if b != expected[b_set] {
                    return false;
                }
                b_set += 1;
                b = 0;
            }
        }
    }

    if b > 0 && b != expected[b_set] {
        return false;
    }

    if (b_set != expected.len() && b_set != expected.len() - 1) || b_count != expected.iter().sum() {
        return false;
    }

    true
}

fn count_p_b(option: &str, expected: usize) -> bool {
    let b_count = option.chars().filter(|&c| c == '1').count();
    b_count == expected
}

fn main_loop(line: &(String, Vec<String>), indx: usize, double: bool) -> (i32, usize) {
    let mut line_t = 0;
    let mut q_count: usize = 0;
    let mut q_pos = Vec::new();
    let mut b_count = 0;
    let mut expected: Vec<usize> = line.1.iter().map(|s| s.parse().unwrap()).collect();
    if double {
        
    let mut n_expected: Vec<usize> = line.1.iter().map(|s| s.parse().unwrap()).collect();
    expected.append(&mut n_expected);
    }
    let expected_b_count: usize = expected.iter().sum();

    let t_line;
    if double {
        t_line = format!("{}?{}",line.0.clone(), line.0.clone());
    } else {
        t_line = line.0.clone();
    }
     

    for (idx, char) in t_line.chars().enumerate() {
        if char == '?' {
            q_count += 1;
            q_pos.push(idx);
        } else if char == '#' {
            b_count += 1;
        }
    }

    let comb_len = q_count;
    for i in 0..2u32.pow(q_count as u32) {
        let mut t_line;
        if double {
            t_line = format!("{}?{}",line.0.clone(), line.0.clone());
        } else {
            t_line = line.0.clone();
        }
        let option = format!("{:0width$b}", i, width = comb_len);
        
        if !count_p_b(&option, expected_b_count - b_count) {
            continue;
        }

        for (idx, pos) in q_pos.iter().enumerate() {
            let replacement = if option.chars().nth(idx).unwrap() == '0' { '.' } else { '#' };
            t_line.replace_range(*pos..=*pos, &replacement.to_string());
        }

        if verify_line(&t_line, &expected) {
            line_t += 1;
        }
    }

    (line_t, indx)
}


fn main() {
    let file = std::fs::read_to_string("input.txt").expect("Unable to read file");
    let lines: Vec<_> = file.lines().map(|line: &str| line.split_whitespace().collect()).collect();
    let lines: Vec<_> = lines.iter().map(|line: &Vec<&str>| (line[0].to_string(), line[1].split(',').map(|s| s.to_string()).collect())).collect();

    let mut o_l_t = vec![0; lines.len()];
    let (sender, receiver) = mpsc::channel();
    let mut threads = vec![];

    let lines_mutex = Arc::new(Mutex::new(lines.clone()));

    for (idx, _) in lines_mutex.lock().unwrap().iter().enumerate() {
        let thread_send = sender.clone();
        let lines_clone = Arc::clone(&lines_mutex);

        threads.push(thread::spawn(move || {
            let (output, index) = main_loop(&lines_clone.lock().unwrap()[idx], idx, false);
            thread_send.send((output, index)).expect("Failed to send");
        }));
    }

    for thread in threads {
        let (result,index) = receiver.recv().expect("failed to receive");
        o_l_t[index] = result;
        thread.join().expect("Failed to join");
    }

    println!("{:?}", o_l_t);

    let mut s_l_t = vec![0; lines.len()];

    let (sender, receiver) = mpsc::channel();
    let mut threads = vec![];

    let lines_mutex = Arc::new(Mutex::new(lines.clone()));

    for (idx, _) in lines_mutex.lock().unwrap().iter().enumerate() {
        let thread_send = sender.clone();
        let lines_clone = Arc::clone(&lines_mutex);

        threads.push(thread::spawn(move || {
            let (output, index) = main_loop(&lines_clone.lock().unwrap()[idx], idx, true);
            thread_send.send((output, index)).expect("Failed to send");
        }));
    }

    for thread in threads {
        let (result,index) = receiver.recv().expect("failed to receive");
        s_l_t[index] = result;
        thread.join().expect("Failed to join");
    }

    println!("{:?}", s_l_t);

    let total: i32 = o_l_t.iter().zip(&s_l_t).map(|(a, b)| a * (b / a).pow(4) as i32).sum();
    println!("{}", total);
}
