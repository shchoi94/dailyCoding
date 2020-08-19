package p14889;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static ArrayList<TeamCase> teamList=new ArrayList<>();
	public static void main(String[] args) throws IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		n=Integer.parseInt(br.readLine());
		boolean[] players=new boolean[n];
		int[][] abilityTable=new int[n][n];
		String temp;
		for(int i=0;i<n;i++){
			temp=br.readLine();
			StringTokenizer st=new StringTokenizer(temp);
			for(int j=0;j<n;j++){
				abilityTable[i][j]=Integer.parseInt(st.nextToken());
			}
		}
//		for(int i=0;i<n;i++){
//			for(int j=0;j<n;j++){
//				System.out.print(abilityTable[i][j]);
//			}
//			System.out.println();
//		}
		Arrays.fill(players,false);
		organizeTeam(0,players,0,abilityTable);
		int min=teamList.get(0).diffTeamStat;
		for(int i=0;i<teamList.size();i++){
			if(min>teamList.get(i).diffTeamStat){
				min=teamList.get(i).diffTeamStat;
			}
			//System.out.print(Arrays.toString(teamList.get(i).team1));
			//System.out.print(Arrays.toString(teamList.get(i).team2));
			//System.out.println();
		}
		System.out.println(min);
	}
	public static void organizeTeam(int depth,boolean[] players,int s,int[][] abilityTable){
		int[] team1=new int[n/2];
		int[] team2=new int[n/2];

		if(depth==n/2){
			int j=0;
			int k=0;
			for(int i=0;i<n;i++){
				if(!players[i]){
					team2[j++]=i;
				}
				if(players[i]){
					team1[k++]=i;
				}
			}
			teamList.add(new TeamCase(team1,team2,abilityTable));
			return;
		}
		for(int i=s;i<n;i++){
			if(!players[i]){
				players[i]=!players[i];
				organizeTeam(depth+1,players,i+1,abilityTable);
				players[i]=!players[i];
			}
		}
		return;
	}
}

class TeamCase{
	int[] team1;
	int[] team2;
	int diffTeamStat=0;

	TeamCase(int[] team1,int[] team2,int[][] abilityTable){
		this.team1=team1;
		this.team2=team2;
		calcTeamStat(abilityTable);

	}

	public void calcTeamStat(int[][] abilityTable){
		int teamStat1=0;
		int teamStat2=0;
		for(int i=0;i<team1.length;i++){
			for(int j=0;j<team1.length;j++){
				if(i!=j){
					teamStat1+=abilityTable[team1[i]][team1[j]];
					teamStat2+=abilityTable[team2[i]][team2[j]];
				}
			}
		}
		if(teamStat1-teamStat2<0){
			diffTeamStat=teamStat2-teamStat1;
		}
		else{
			diffTeamStat=teamStat1-teamStat2;
		}
	}

}
