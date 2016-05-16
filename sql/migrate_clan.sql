INSERT INTO clan_list (clan_id, create_date, status, clan_name, clan_tag, clan_founder_id, clan_leader_id, clan_desc)
SELECT clan_id, create_date, status, clan_name, clan_tag, clan_founder_id, (SELECT player_id FROM fafclans.clan_leader l WHERE l.clan_id = a.clan_id LIMIT 1) clan_leader_id, clan_desc 
FROM fafclans.clans_list a;

INSERT INTO clan_members (clan_id, player_id, join_clan_date)
SELECT clan_id, player_id, join_clan_date 
FROM fafclans.clan_members;
