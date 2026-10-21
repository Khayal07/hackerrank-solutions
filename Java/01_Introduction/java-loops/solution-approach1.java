// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/challenges/java-loops/problem?isFullScreen=true
// Problem     Java Loops II
// Difficulty  Easy
// Subdomain   Introduction
// Platform    HackerRank
// Language    java
// Status      Accepted
// Submitted   2026-10-22, 12:25 a.m.
// ──────────────────────────────────────────────────

import java.util.*;
import java.io.*;

class Solution {
    public static void main(String []argh) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int i = 0; i < t; i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            int currentSum = a;
            for (int j = 0; j < n; j++) {
                currentSum += (1 << j) * b;
                System.out.print(currentSum + " ");
            }
            System.out.println();
        }
        in.close();
    }
}
