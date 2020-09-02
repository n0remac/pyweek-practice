from typing import Union
from pathlib import Path
from . import shaders

#: The absolute path to this directory
RESOURCE_PATH = Path(__file__).parent.absolute()


def resolve_resource_path(path: Union[str, Path]) -> Path:
    """Resolves a resource path and returns a Path object.

    :param Union[str, Path] path: A Path or string
    """
    # Convert to a Path object and resolve :resources:
    if isinstance(path, str):
        path = path.strip()  # Allow for silly mistakes with extra spaces
        if path.startswith(':resources:'):
            path = path[11:]
            while path.startswith('/') or path.startswith('\\'):
                path = path[1:]

            # Always convert into a Path object
            path = Path(RESOURCE_PATH / path)
        else:
            path = Path(path)

    # Check for the existence of the file and provide useful feedback to
    # avoid deep stack trace into pathlib
    if not path.exists():
        raise FileNotFoundError(f"Cannot locate resource : {path}")

    # Always return absolute paths
    return path.absolute()


# RESOURCE LIST : (Truncate file from here if auto generating resource list)
gui_clicked = ':resources:/gui_themes/Fantasy/Buttons/Clicked.png'
gui_hover = ':resources:/gui_themes/Fantasy/Buttons/Hover.png'
gui_locked = ':resources:/gui_themes/Fantasy/Buttons/Locked.png'
gui_normal = ':resources:/gui_themes/Fantasy/Buttons/Normal.png'
gui_dialogue_box = ':resources:/gui_themes/Fantasy/DialogueBox/DialogueBox.png'
gui_menu = ':resources:/gui_themes/Fantasy/Menu/Menu.png'
gui_brown = ':resources:/gui_themes/Fantasy/TextBox/Brown.png'
gui_light_brown = ':resources:/gui_themes/Fantasy/TextBox/LightBrown.png'
gui_window = ':resources:/gui_themes/Fantasy/Window/Window.png'
image_alien_blue_climb1 = ':resources:/images/alien/alienBlue_climb1.png'
image_alien_blue_climb2 = ':resources:/images/alien/alienBlue_climb2.png'
image_alien_blue_front = ':resources:/images/alien/alienBlue_front.png'
image_alien_blue_jump = ':resources:/images/alien/alienBlue_jump.png'
image_alien_blue_walk1 = ':resources:/images/alien/alienBlue_walk1.png'
image_alien_blue_walk2 = ':resources:/images/alien/alienBlue_walk2.png'
image_female_adventurer_climb0 = ':resources:/images/animated_characters/female_adventurer/femaleAdventurer_climb0.png'
image_female_adventurer_climb1 = ':resources:/images/animated_characters/female_adventurer/femaleAdventurer_climb1.png'
image_female_adventurer_fall = ':resources:/images/animated_characters/female_adventurer/femaleAdventurer_fall.png'
image_female_adventurer_idle = ':resources:/images/animated_characters/female_adventurer/femaleAdventurer_idle.png'
image_female_adventurer_jump = ':resources:/images/animated_characters/female_adventurer/femaleAdventurer_jump.png'
image_female_adventurer_walk0 = ':resources:/images/animated_characters/female_adventurer/femaleAdventurer_walk0.png'
image_female_adventurer_walk1 = ':resources:/images/animated_characters/female_adventurer/femaleAdventurer_walk1.png'
image_female_adventurer_walk2 = ':resources:/images/animated_characters/female_adventurer/femaleAdventurer_walk2.png'
image_female_adventurer_walk3 = ':resources:/images/animated_characters/female_adventurer/femaleAdventurer_walk3.png'
image_female_adventurer_walk4 = ':resources:/images/animated_characters/female_adventurer/femaleAdventurer_walk4.png'
image_female_adventurer_walk5 = ':resources:/images/animated_characters/female_adventurer/femaleAdventurer_walk5.png'
image_female_adventurer_walk6 = ':resources:/images/animated_characters/female_adventurer/femaleAdventurer_walk6.png'
image_female_adventurer_walk7 = ':resources:/images/animated_characters/female_adventurer/femaleAdventurer_walk7.png'
image_female_person_climb0 = ':resources:/images/animated_characters/female_person/femalePerson_climb0.png'
image_female_person_climb1 = ':resources:/images/animated_characters/female_person/femalePerson_climb1.png'
image_female_person_fall = ':resources:/images/animated_characters/female_person/femalePerson_fall.png'
image_female_person_idle = ':resources:/images/animated_characters/female_person/femalePerson_idle.png'
image_female_person_jump = ':resources:/images/animated_characters/female_person/femalePerson_jump.png'
image_female_person_walk0 = ':resources:/images/animated_characters/female_person/femalePerson_walk0.png'
image_female_person_walk1 = ':resources:/images/animated_characters/female_person/femalePerson_walk1.png'
image_female_person_walk2 = ':resources:/images/animated_characters/female_person/femalePerson_walk2.png'
image_female_person_walk3 = ':resources:/images/animated_characters/female_person/femalePerson_walk3.png'
image_female_person_walk4 = ':resources:/images/animated_characters/female_person/femalePerson_walk4.png'
image_female_person_walk5 = ':resources:/images/animated_characters/female_person/femalePerson_walk5.png'
image_female_person_walk6 = ':resources:/images/animated_characters/female_person/femalePerson_walk6.png'
image_female_person_walk7 = ':resources:/images/animated_characters/female_person/femalePerson_walk7.png'
image_male_adventurer_climb0 = ':resources:/images/animated_characters/male_adventurer/maleAdventurer_climb0.png'
image_male_adventurer_climb1 = ':resources:/images/animated_characters/male_adventurer/maleAdventurer_climb1.png'
image_male_adventurer_fall = ':resources:/images/animated_characters/male_adventurer/maleAdventurer_fall.png'
image_male_adventurer_idle = ':resources:/images/animated_characters/male_adventurer/maleAdventurer_idle.png'
image_male_adventurer_jump = ':resources:/images/animated_characters/male_adventurer/maleAdventurer_jump.png'
image_male_adventurer_walk0 = ':resources:/images/animated_characters/male_adventurer/maleAdventurer_walk0.png'
image_male_adventurer_walk1 = ':resources:/images/animated_characters/male_adventurer/maleAdventurer_walk1.png'
image_male_adventurer_walk2 = ':resources:/images/animated_characters/male_adventurer/maleAdventurer_walk2.png'
image_male_adventurer_walk3 = ':resources:/images/animated_characters/male_adventurer/maleAdventurer_walk3.png'
image_male_adventurer_walk4 = ':resources:/images/animated_characters/male_adventurer/maleAdventurer_walk4.png'
image_male_adventurer_walk5 = ':resources:/images/animated_characters/male_adventurer/maleAdventurer_walk5.png'
image_male_adventurer_walk6 = ':resources:/images/animated_characters/male_adventurer/maleAdventurer_walk6.png'
image_male_adventurer_walk7 = ':resources:/images/animated_characters/male_adventurer/maleAdventurer_walk7.png'
image_male_person_climb0 = ':resources:/images/animated_characters/male_person/malePerson_climb0.png'
image_male_person_climb1 = ':resources:/images/animated_characters/male_person/malePerson_climb1.png'
image_male_person_fall = ':resources:/images/animated_characters/male_person/malePerson_fall.png'
image_male_person_idle = ':resources:/images/animated_characters/male_person/malePerson_idle.png'
image_male_person_jump = ':resources:/images/animated_characters/male_person/malePerson_jump.png'
image_male_person_walk0 = ':resources:/images/animated_characters/male_person/malePerson_walk0.png'
image_male_person_walk1 = ':resources:/images/animated_characters/male_person/malePerson_walk1.png'
image_male_person_walk2 = ':resources:/images/animated_characters/male_person/malePerson_walk2.png'
image_male_person_walk3 = ':resources:/images/animated_characters/male_person/malePerson_walk3.png'
image_male_person_walk4 = ':resources:/images/animated_characters/male_person/malePerson_walk4.png'
image_male_person_walk5 = ':resources:/images/animated_characters/male_person/malePerson_walk5.png'
image_male_person_walk6 = ':resources:/images/animated_characters/male_person/malePerson_walk6.png'
image_male_person_walk7 = ':resources:/images/animated_characters/male_person/malePerson_walk7.png'
image_robot_climb0 = ':resources:/images/animated_characters/robot/robot_climb0.png'
image_robot_climb1 = ':resources:/images/animated_characters/robot/robot_climb1.png'
image_robot_fall = ':resources:/images/animated_characters/robot/robot_fall.png'
image_robot_idle = ':resources:/images/animated_characters/robot/robot_idle.png'
image_robot_jump = ':resources:/images/animated_characters/robot/robot_jump.png'
image_robot_walk0 = ':resources:/images/animated_characters/robot/robot_walk0.png'
image_robot_walk1 = ':resources:/images/animated_characters/robot/robot_walk1.png'
image_robot_walk2 = ':resources:/images/animated_characters/robot/robot_walk2.png'
image_robot_walk3 = ':resources:/images/animated_characters/robot/robot_walk3.png'
image_robot_walk4 = ':resources:/images/animated_characters/robot/robot_walk4.png'
image_robot_walk5 = ':resources:/images/animated_characters/robot/robot_walk5.png'
image_robot_walk6 = ':resources:/images/animated_characters/robot/robot_walk6.png'
image_robot_walk7 = ':resources:/images/animated_characters/robot/robot_walk7.png'
image_zombie_climb0 = ':resources:/images/animated_characters/zombie/zombie_climb0.png'
image_zombie_climb1 = ':resources:/images/animated_characters/zombie/zombie_climb1.png'
image_zombie_fall = ':resources:/images/animated_characters/zombie/zombie_fall.png'
image_zombie_idle = ':resources:/images/animated_characters/zombie/zombie_idle.png'
image_zombie_jump = ':resources:/images/animated_characters/zombie/zombie_jump.png'
image_zombie_walk0 = ':resources:/images/animated_characters/zombie/zombie_walk0.png'
image_zombie_walk1 = ':resources:/images/animated_characters/zombie/zombie_walk1.png'
image_zombie_walk2 = ':resources:/images/animated_characters/zombie/zombie_walk2.png'
image_zombie_walk3 = ':resources:/images/animated_characters/zombie/zombie_walk3.png'
image_zombie_walk4 = ':resources:/images/animated_characters/zombie/zombie_walk4.png'
image_zombie_walk5 = ':resources:/images/animated_characters/zombie/zombie_walk5.png'
image_zombie_walk6 = ':resources:/images/animated_characters/zombie/zombie_walk6.png'
image_zombie_walk7 = ':resources:/images/animated_characters/zombie/zombie_walk7.png'
image_instructions_0 = ':resources:/images/backgrounds/instructions_0.png'
image_instructions_1 = ':resources:/images/backgrounds/instructions_1.png'
image_bee = ':resources:/images/enemies/bee.png'
image_fish_green = ':resources:/images/enemies/fishGreen.png'
image_fish_pink = ':resources:/images/enemies/fishPink.png'
image_fly = ':resources:/images/enemies/fly.png'
image_frog = ':resources:/images/enemies/frog.png'
image_frog_move = ':resources:/images/enemies/frog_move.png'
image_ladybug = ':resources:/images/enemies/ladybug.png'
image_mouse = ':resources:/images/enemies/mouse.png'
image_saw = ':resources:/images/enemies/saw.png'
image_saw_half = ':resources:/images/enemies/sawHalf.png'
image_slime_block = ':resources:/images/enemies/slimeBlock.png'
image_slime_blue = ':resources:/images/enemies/slimeBlue.png'
image_slime_blue_move = ':resources:/images/enemies/slimeBlue_move.png'
image_slime_green = ':resources:/images/enemies/slimeGreen.png'
image_slime_purple = ':resources:/images/enemies/slimePurple.png'
image_worm_green = ':resources:/images/enemies/wormGreen.png'
image_worm_green_dead = ':resources:/images/enemies/wormGreen_dead.png'
image_worm_green_move = ':resources:/images/enemies/wormGreen_move.png'
image_worm_pink = ':resources:/images/enemies/wormPink.png'
image_dirt_tiles_s = ':resources:/images/isometric_dungeon/dirtTiles_S.png'
image_dirt_s = ':resources:/images/isometric_dungeon/dirt_S.png'
image_stone_left_n = ':resources:/images/isometric_dungeon/stoneLeft_N.png'
image_stone_missing_tiles_e = ':resources:/images/isometric_dungeon/stoneMissingTiles_E.png'
image_stone_missing_tiles_n = ':resources:/images/isometric_dungeon/stoneMissingTiles_N.png'
image_stone_missing_tiles_s = ':resources:/images/isometric_dungeon/stoneMissingTiles_S.png'
image_stone_missing_tiles_w = ':resources:/images/isometric_dungeon/stoneMissingTiles_W.png'
image_stone_side_uneven_n = ':resources:/images/isometric_dungeon/stoneSideUneven_N.png'
image_stone_side_e = ':resources:/images/isometric_dungeon/stoneSide_E.png'
image_stone_tile_n = ':resources:/images/isometric_dungeon/stoneTile_N.png'
image_stone_tile_s = ':resources:/images/isometric_dungeon/stoneTile_S.png'
image_stone_tile_w = ':resources:/images/isometric_dungeon/stoneTile_W.png'
image_stone_uneven_e = ':resources:/images/isometric_dungeon/stoneUneven_E.png'
image_stone_uneven_n = ':resources:/images/isometric_dungeon/stoneUneven_N.png'
image_stone_uneven_s = ':resources:/images/isometric_dungeon/stoneUneven_S.png'
image_stone_uneven_w = ':resources:/images/isometric_dungeon/stoneUneven_W.png'
image_stone_wall_aged_e = ':resources:/images/isometric_dungeon/stoneWallAged_E.png'
image_stone_wall_aged_s = ':resources:/images/isometric_dungeon/stoneWallAged_S.png'
image_stone_wall_archway_s = ':resources:/images/isometric_dungeon/stoneWallArchway_S.png'
image_stone_wall_column_e = ':resources:/images/isometric_dungeon/stoneWallColumn_E.png'
image_stone_wall_corner_e = ':resources:/images/isometric_dungeon/stoneWallCorner_E.png'
image_stone_wall_corner_n = ':resources:/images/isometric_dungeon/stoneWallCorner_N.png'
image_stone_wall_corner_s = ':resources:/images/isometric_dungeon/stoneWallCorner_S.png'
image_stone_wall_corner_w = ':resources:/images/isometric_dungeon/stoneWallCorner_W.png'
image_stone_wall_gate_closed_e = ':resources:/images/isometric_dungeon/stoneWallGateClosed_E.png'
image_stone_wall_gate_closed_s = ':resources:/images/isometric_dungeon/stoneWallGateClosed_S.png'
image_stone_wall_gate_open_e = ':resources:/images/isometric_dungeon/stoneWallGateOpen_E.png'
image_stone_wall_n = ':resources:/images/isometric_dungeon/stoneWall_N.png'
image_stone_wall_s = ':resources:/images/isometric_dungeon/stoneWall_S.png'
image_stone_wall_w = ':resources:/images/isometric_dungeon/stoneWall_W.png'
image_stone_e = ':resources:/images/isometric_dungeon/stone_E.png'
image_stone_n = ':resources:/images/isometric_dungeon/stone_N.png'
image_stone_s = ':resources:/images/isometric_dungeon/stone_S.png'
image_stone_w = ':resources:/images/isometric_dungeon/stone_W.png'
image_table_chairs_broken_e = ':resources:/images/isometric_dungeon/tableChairsBroken_E.png'
image_table_chairs_broken_s = ':resources:/images/isometric_dungeon/tableChairsBroken_S.png'
image_table_short_chairs_w = ':resources:/images/isometric_dungeon/tableShortChairs_W.png'
image_wooden_crates_w = ':resources:/images/isometric_dungeon/woodenCrates_W.png'
image_wooden_support_beams_s = ':resources:/images/isometric_dungeon/woodenSupportBeams_S.png'
image_wooden_supports_beam_s = ':resources:/images/isometric_dungeon/woodenSupportsBeam_S.png'
image_coin_bronze = ':resources:/images/items/coinBronze.png'
image_coin_gold = ':resources:/images/items/coinGold.png'
image_coin_gold_ll = ':resources:/images/items/coinGold_ll.png'
image_coin_gold_lr = ':resources:/images/items/coinGold_lr.png'
image_coin_gold_ul = ':resources:/images/items/coinGold_ul.png'
image_coin_gold_ur = ':resources:/images/items/coinGold_ur.png'
image_coin_silver = ':resources:/images/items/coinSilver.png'
image_coin_silver_test = ':resources:/images/items/coinSilver_test.png'
image_flag_green1 = ':resources:/images/items/flagGreen1.png'
image_flag_green2 = ':resources:/images/items/flagGreen2.png'
image_flag_green_down = ':resources:/images/items/flagGreen_down.png'
image_flag_red1 = ':resources:/images/items/flagRed1.png'
image_flag_red2 = ':resources:/images/items/flagRed2.png'
image_flag_red_down = ':resources:/images/items/flagRed_down.png'
image_flag_yellow1 = ':resources:/images/items/flagYellow1.png'
image_flag_yellow2 = ':resources:/images/items/flagYellow2.png'
image_flag_yellow_down = ':resources:/images/items/flagYellow_down.png'
image_gem_blue = ':resources:/images/items/gemBlue.png'
image_gem_green = ':resources:/images/items/gemGreen.png'
image_gem_red = ':resources:/images/items/gemRed.png'
image_gem_yellow = ':resources:/images/items/gemYellow.png'
image_gold_1 = ':resources:/images/items/gold_1.png'
image_gold_2 = ':resources:/images/items/gold_2.png'
image_gold_3 = ':resources:/images/items/gold_3.png'
image_gold_4 = ':resources:/images/items/gold_4.png'
image_key_blue = ':resources:/images/items/keyBlue.png'
image_key_green = ':resources:/images/items/keyGreen.png'
image_key_red = ':resources:/images/items/keyRed.png'
image_key_yellow = ':resources:/images/items/keyYellow.png'
image_ladder_mid = ':resources:/images/items/ladderMid.png'
image_ladder_top = ':resources:/images/items/ladderTop.png'
image_star = ':resources:/images/items/star.png'
image_bumper = ':resources:/images/pinball/bumper.png'
image_pool_cue_ball = ':resources:/images/pinball/pool_cue_ball.png'
image_laser_blue01 = ':resources:/images/space_shooter/laserBlue01.png'
image_laser_red01 = ':resources:/images/space_shooter/laserRed01.png'
image_meteor_grey_big1 = ':resources:/images/space_shooter/meteorGrey_big1.png'
image_meteor_grey_big2 = ':resources:/images/space_shooter/meteorGrey_big2.png'
image_meteor_grey_big3 = ':resources:/images/space_shooter/meteorGrey_big3.png'
image_meteor_grey_big4 = ':resources:/images/space_shooter/meteorGrey_big4.png'
image_meteor_grey_med1 = ':resources:/images/space_shooter/meteorGrey_med1.png'
image_meteor_grey_med2 = ':resources:/images/space_shooter/meteorGrey_med2.png'
image_meteor_grey_small1 = ':resources:/images/space_shooter/meteorGrey_small1.png'
image_meteor_grey_small2 = ':resources:/images/space_shooter/meteorGrey_small2.png'
image_meteor_grey_tiny1 = ':resources:/images/space_shooter/meteorGrey_tiny1.png'
image_meteor_grey_tiny2 = ':resources:/images/space_shooter/meteorGrey_tiny2.png'
image_player_life1_orange = ':resources:/images/space_shooter/playerLife1_orange.png'
image_player_ship1_green = ':resources:/images/space_shooter/playerShip1_green.png'
image_player_ship1_orange = ':resources:/images/space_shooter/playerShip1_orange.png'
image_player_ship2_orange = ':resources:/images/space_shooter/playerShip2_orange.png'
image_player_ship3_orange = ':resources:/images/space_shooter/playerShip3_orange.png'
image_explosion = ':resources:/images/spritesheets/explosion.png'
image_number_sheet = ':resources:/images/spritesheets/number_sheet.png'
image_tiles = ':resources:/images/spritesheets/tiles.png'
image_box_crate = ':resources:/images/tiles/boxCrate.png'
image_box_crate_double = ':resources:/images/tiles/boxCrate_double.png'
image_box_crate_single = ':resources:/images/tiles/boxCrate_single.png'
image_brick_brown = ':resources:/images/tiles/brickBrown.png'
image_brick_grey = ':resources:/images/tiles/brickGrey.png'
image_bridge_a = ':resources:/images/tiles/bridgeA.png'
image_bridge_b = ':resources:/images/tiles/bridgeB.png'
image_bush = ':resources:/images/tiles/bush.png'
image_cactus = ':resources:/images/tiles/cactus.png'
image_dirt = ':resources:/images/tiles/dirt.png'
image_dirt_center = ':resources:/images/tiles/dirtCenter.png'
image_dirt_center_rounded = ':resources:/images/tiles/dirtCenter_rounded.png'
image_dirt_cliff_alt_left = ':resources:/images/tiles/dirtCliffAlt_left.png'
image_dirt_cliff_alt_right = ':resources:/images/tiles/dirtCliffAlt_right.png'
image_dirt_cliff_left = ':resources:/images/tiles/dirtCliff_left.png'
image_dirt_cliff_right = ':resources:/images/tiles/dirtCliff_right.png'
image_dirt_corner_left = ':resources:/images/tiles/dirtCorner_left.png'
image_dirt_corner_right = ':resources:/images/tiles/dirtCorner_right.png'
image_dirt_half = ':resources:/images/tiles/dirtHalf.png'
image_dirt_half_left = ':resources:/images/tiles/dirtHalf_left.png'
image_dirt_half_mid = ':resources:/images/tiles/dirtHalf_mid.png'
image_dirt_half_right = ':resources:/images/tiles/dirtHalf_right.png'
image_dirt_hill_left = ':resources:/images/tiles/dirtHill_left.png'
image_dirt_hill_right = ':resources:/images/tiles/dirtHill_right.png'
image_dirt_left = ':resources:/images/tiles/dirtLeft.png'
image_dirt_mid = ':resources:/images/tiles/dirtMid.png'
image_dirt_right = ':resources:/images/tiles/dirtRight.png'
image_door_closed_mid = ':resources:/images/tiles/doorClosed_mid.png'
image_door_closed_top = ':resources:/images/tiles/doorClosed_top.png'
image_grass = ':resources:/images/tiles/grass.png'
image_grass_center = ':resources:/images/tiles/grassCenter.png'
image_grass_center_round = ':resources:/images/tiles/grassCenter_round.png'
image_grass_cliff_alt_left = ':resources:/images/tiles/grassCliffAlt_left.png'
image_grass_cliff_alt_right = ':resources:/images/tiles/grassCliffAlt_right.png'
image_grass_cliff_left = ':resources:/images/tiles/grassCliff_left.png'
image_grass_cliff_right = ':resources:/images/tiles/grassCliff_right.png'
image_grass_corner_left = ':resources:/images/tiles/grassCorner_left.png'
image_grass_corner_right = ':resources:/images/tiles/grassCorner_right.png'
image_grass_half = ':resources:/images/tiles/grassHalf.png'
image_grass_half_left = ':resources:/images/tiles/grassHalf_left.png'
image_grass_half_mid = ':resources:/images/tiles/grassHalf_mid.png'
image_grass_half_right = ':resources:/images/tiles/grassHalf_right.png'
image_grass_hill_left = ':resources:/images/tiles/grassHill_left.png'
image_grass_hill_right = ':resources:/images/tiles/grassHill_right.png'
image_grass_left = ':resources:/images/tiles/grassLeft.png'
image_grass_mid = ':resources:/images/tiles/grassMid.png'
image_grass_right = ':resources:/images/tiles/grassRight.png'
image_grass_sprout = ':resources:/images/tiles/grass_sprout.png'
image_ladder_mid = ':resources:/images/tiles/ladderMid.png'
image_ladder_top = ':resources:/images/tiles/ladderTop.png'
image_lava = ':resources:/images/tiles/lava.png'
image_lava_top_high = ':resources:/images/tiles/lavaTop_high.png'
image_lava_top_low = ':resources:/images/tiles/lavaTop_low.png'
image_lever_left = ':resources:/images/tiles/leverLeft.png'
image_lever_mid = ':resources:/images/tiles/leverMid.png'
image_lever_right = ':resources:/images/tiles/leverRight.png'
image_lock_red = ':resources:/images/tiles/lockRed.png'
image_lock_yellow = ':resources:/images/tiles/lockYellow.png'
image_mushroom_red = ':resources:/images/tiles/mushroomRed.png'
image_planet = ':resources:/images/tiles/planet.png'
image_planet_center = ':resources:/images/tiles/planetCenter.png'
image_planet_center_rounded = ':resources:/images/tiles/planetCenter_rounded.png'
image_planet_cliff_alt_left = ':resources:/images/tiles/planetCliffAlt_left.png'
image_planet_cliff_alt_right = ':resources:/images/tiles/planetCliffAlt_right.png'
image_planet_cliff_left = ':resources:/images/tiles/planetCliff_left.png'
image_planet_cliff_right = ':resources:/images/tiles/planetCliff_right.png'
image_planet_corner_left = ':resources:/images/tiles/planetCorner_left.png'
image_planet_corner_right = ':resources:/images/tiles/planetCorner_right.png'
image_planet_half = ':resources:/images/tiles/planetHalf.png'
image_planet_half_left = ':resources:/images/tiles/planetHalf_left.png'
image_planet_half_mid = ':resources:/images/tiles/planetHalf_mid.png'
image_planet_half_right = ':resources:/images/tiles/planetHalf_right.png'
image_planet_hill_left = ':resources:/images/tiles/planetHill_left.png'
image_planet_hill_right = ':resources:/images/tiles/planetHill_right.png'
image_planet_left = ':resources:/images/tiles/planetLeft.png'
image_planet_mid = ':resources:/images/tiles/planetMid.png'
image_planet_right = ':resources:/images/tiles/planetRight.png'
image_plant_purple = ':resources:/images/tiles/plantPurple.png'
image_rock = ':resources:/images/tiles/rock.png'
image_sand = ':resources:/images/tiles/sand.png'
image_sand_center = ':resources:/images/tiles/sandCenter.png'
image_sand_center_rounded = ':resources:/images/tiles/sandCenter_rounded.png'
image_sand_cliff_alt_left = ':resources:/images/tiles/sandCliffAlt_left.png'
image_sand_cliff_alt_right = ':resources:/images/tiles/sandCliffAlt_right.png'
image_sand_cliff_left = ':resources:/images/tiles/sandCliff_left.png'
image_sand_cliff_right = ':resources:/images/tiles/sandCliff_right.png'
image_sand_corner_leftg = ':resources:/images/tiles/sandCorner_leftg.png'
image_sand_corner_right = ':resources:/images/tiles/sandCorner_right.png'
image_sand_half = ':resources:/images/tiles/sandHalf.png'
image_sand_half_left = ':resources:/images/tiles/sandHalf_left.png'
image_sand_half_mid = ':resources:/images/tiles/sandHalf_mid.png'
image_sand_half_right = ':resources:/images/tiles/sandHalf_right.png'
image_sand_hill_left = ':resources:/images/tiles/sandHill_left.png'
image_sand_hill_right = ':resources:/images/tiles/sandHill_right.png'
image_sand_left = ':resources:/images/tiles/sandLeft.png'
image_sand_mid = ':resources:/images/tiles/sandMid.png'
image_sand_right = ':resources:/images/tiles/sandRight.png'
image_sign_exit = ':resources:/images/tiles/signExit.png'
image_sign_left = ':resources:/images/tiles/signLeft.png'
image_sign_right = ':resources:/images/tiles/signRight.png'
image_snow = ':resources:/images/tiles/snow.png'
image_snow_center = ':resources:/images/tiles/snowCenter.png'
image_snow_center_rounded = ':resources:/images/tiles/snowCenter_rounded.png'
image_snow_cliff_alt_left = ':resources:/images/tiles/snowCliffAlt_left.png'
image_snow_cliff_alt_right = ':resources:/images/tiles/snowCliffAlt_right.png'
image_snow_cliff_left = ':resources:/images/tiles/snowCliff_left.png'
image_snow_cliff_right = ':resources:/images/tiles/snowCliff_right.png'
image_snow_corner_left = ':resources:/images/tiles/snowCorner_left.png'
image_snow_corner_right = ':resources:/images/tiles/snowCorner_right.png'
image_snow_half = ':resources:/images/tiles/snowHalf.png'
image_snow_half_left = ':resources:/images/tiles/snowHalf_left.png'
image_snow_half_mid = ':resources:/images/tiles/snowHalf_mid.png'
image_snow_half_right = ':resources:/images/tiles/snowHalf_right.png'
image_snow_hill_left = ':resources:/images/tiles/snowHill_left.png'
image_snow_hill_right = ':resources:/images/tiles/snowHill_right.png'
image_snow_left = ':resources:/images/tiles/snowLeft.png'
image_snow_mid = ':resources:/images/tiles/snowMid.png'
image_snow_right = ':resources:/images/tiles/snowRight.png'
image_snow_pile = ':resources:/images/tiles/snow_pile.png'
image_spikes = ':resources:/images/tiles/spikes.png'
image_stone = ':resources:/images/tiles/stone.png'
image_stone_center = ':resources:/images/tiles/stoneCenter.png'
image_stone_center_rounded = ':resources:/images/tiles/stoneCenter_rounded.png'
image_stone_cliff_alt_left = ':resources:/images/tiles/stoneCliffAlt_left.png'
image_stone_cliff_alt_right = ':resources:/images/tiles/stoneCliffAlt_right.png'
image_stone_cliff_left = ':resources:/images/tiles/stoneCliff_left.png'
image_stone_cliff_right = ':resources:/images/tiles/stoneCliff_right.png'
image_stone_corner_left = ':resources:/images/tiles/stoneCorner_left.png'
image_stone_corner_right = ':resources:/images/tiles/stoneCorner_right.png'
image_stone_half = ':resources:/images/tiles/stoneHalf.png'
image_stone_half_left = ':resources:/images/tiles/stoneHalf_left.png'
image_stone_half_mid = ':resources:/images/tiles/stoneHalf_mid.png'
image_stone_half_right = ':resources:/images/tiles/stoneHalf_right.png'
image_stone_hill_left = ':resources:/images/tiles/stoneHill_left.png'
image_stone_hill_right = ':resources:/images/tiles/stoneHill_right.png'
image_stone_left = ':resources:/images/tiles/stoneLeft.png'
image_stone_mid = ':resources:/images/tiles/stoneMid.png'
image_stone_right = ':resources:/images/tiles/stoneRight.png'
image_switch_green = ':resources:/images/tiles/switchGreen.png'
image_switch_green_pressed = ':resources:/images/tiles/switchGreen_pressed.png'
image_switch_red = ':resources:/images/tiles/switchRed.png'
image_switch_red_pressed = ':resources:/images/tiles/switchRed_pressed.png'
image_torch1 = ':resources:/images/tiles/torch1.png'
image_torch2 = ':resources:/images/tiles/torch2.png'
image_torch_off = ':resources:/images/tiles/torchOff.png'
image_water = ':resources:/images/tiles/water.png'
image_water_top_high = ':resources:/images/tiles/waterTop_high.png'
image_water_top_low = ':resources:/images/tiles/waterTop_low.png'
sound_coin1 = ':resources:/sounds/coin1.wav'
sound_coin2 = ':resources:/sounds/coin2.wav'
sound_coin3 = ':resources:/sounds/coin3.wav'
sound_coin4 = ':resources:/sounds/coin4.wav'
sound_coin5 = ':resources:/sounds/coin5.wav'
sound_error1 = ':resources:/sounds/error1.wav'
sound_error2 = ':resources:/sounds/error2.wav'
sound_error3 = ':resources:/sounds/error3.wav'
sound_error4 = ':resources:/sounds/error4.wav'
sound_error5 = ':resources:/sounds/error5.wav'
sound_explosion1 = ':resources:/sounds/explosion1.wav'
sound_explosion2 = ':resources:/sounds/explosion2.wav'
sound_fall1 = ':resources:/sounds/fall1.wav'
sound_fall2 = ':resources:/sounds/fall2.wav'
sound_fall3 = ':resources:/sounds/fall3.wav'
sound_fall4 = ':resources:/sounds/fall4.wav'
sound_gameover1 = ':resources:/sounds/gameover1.wav'
sound_gameover2 = ':resources:/sounds/gameover2.wav'
sound_gameover3 = ':resources:/sounds/gameover3.wav'
sound_gameover4 = ':resources:/sounds/gameover4.wav'
sound_gameover5 = ':resources:/sounds/gameover5.wav'
sound_hit1 = ':resources:/sounds/hit1.wav'
sound_hit2 = ':resources:/sounds/hit2.wav'
sound_hit3 = ':resources:/sounds/hit3.wav'
sound_hit4 = ':resources:/sounds/hit4.wav'
sound_hit5 = ':resources:/sounds/hit5.wav'
sound_hurt1 = ':resources:/sounds/hurt1.wav'
sound_hurt2 = ':resources:/sounds/hurt2.wav'
sound_hurt3 = ':resources:/sounds/hurt3.wav'
sound_hurt4 = ':resources:/sounds/hurt4.wav'
sound_hurt5 = ':resources:/sounds/hurt5.wav'
sound_jump1 = ':resources:/sounds/jump1.wav'
sound_jump2 = ':resources:/sounds/jump2.wav'
sound_jump3 = ':resources:/sounds/jump3.wav'
sound_jump4 = ':resources:/sounds/jump4.wav'
sound_jump5 = ':resources:/sounds/jump5.wav'
sound_laser1 = ':resources:/sounds/laser1.mp3'
sound_laser1 = ':resources:/sounds/laser1.ogg'
sound_laser1 = ':resources:/sounds/laser1.wav'
sound_laser2 = ':resources:/sounds/laser2.wav'
sound_laser3 = ':resources:/sounds/laser3.wav'
sound_laser4 = ':resources:/sounds/laser4.wav'
sound_laser5 = ':resources:/sounds/laser5.wav'
sound_lose1 = ':resources:/sounds/lose1.wav'
sound_lose2 = ':resources:/sounds/lose2.wav'
sound_lose3 = ':resources:/sounds/lose3.wav'
sound_lose4 = ':resources:/sounds/lose4.wav'
sound_lose5 = ':resources:/sounds/lose5.wav'
sound_phase_jump1 = ':resources:/sounds/phaseJump1.ogg'
sound_phase_jump1 = ':resources:/sounds/phaseJump1.wav'
sound_rock_hit2 = ':resources:/sounds/rockHit2.ogg'
sound_rock_hit2 = ':resources:/sounds/rockHit2.wav'
sound_secret2 = ':resources:/sounds/secret2.wav'
sound_secret4 = ':resources:/sounds/secret4.wav'
sound_upgrade1 = ':resources:/sounds/upgrade1.wav'
sound_upgrade2 = ':resources:/sounds/upgrade2.wav'
sound_upgrade3 = ':resources:/sounds/upgrade3.wav'
sound_upgrade4 = ':resources:/sounds/upgrade4.wav'
sound_upgrade5 = ':resources:/sounds/upgrade5.wav'
map_dirt = ':resources:/tmx_maps/dirt.tsx'
map_grass = ':resources:/tmx_maps/grass.tsx'
map_isometric_dungeon = ':resources:/tmx_maps/isometric_dungeon.tmx'
map_items = ':resources:/tmx_maps/items.tsx'
map_level_1 = ':resources:/tmx_maps/level_1.tmx'
map_level_2 = ':resources:/tmx_maps/level_2.tmx'
map_map = ':resources:/tmx_maps/map.tmx'
map_map2_level_1 = ':resources:/tmx_maps/map2_level_1.tmx'
map_map2_level_2 = ':resources:/tmx_maps/map2_level_2.tmx'
map_map_with_custom_hitboxes = ':resources:/tmx_maps/map_with_custom_hitboxes.tmx'
map_map_with_external_tileset = ':resources:/tmx_maps/map_with_external_tileset.tmx'
map_map_with_ladders = ':resources:/tmx_maps/map_with_ladders.tmx'
map_more_tiles = ':resources:/tmx_maps/more_tiles.tsx'
map_spritesheet = ':resources:/tmx_maps/spritesheet.tsx'
map_standard_tileset = ':resources:/tmx_maps/standard_tileset.tsx'
map_test_map_1 = ':resources:/tmx_maps/test_map_1.tmx'
map_test_map_2 = ':resources:/tmx_maps/test_map_2.tmx'
map_test_map_3 = ':resources:/tmx_maps/test_map_3.tmx'
map_test_map_4 = ':resources:/tmx_maps/test_map_4.tmx'
map_test_map_5 = ':resources:/tmx_maps/test_map_5.tmx'
map_test_map_6 = ':resources:/tmx_maps/test_map_6.tmx'
map_test_map_7 = ':resources:/tmx_maps/test_map_7.tmx'