def makeRender(variations,the_color):
    simulation_on = False
    simulation_on = True
    ##############################
    from importlib import reload
    import pyphysicssandbox
    reload(pyphysicssandbox)
    from pyphysicssandbox import Color, rgb_to_normalized,cosmetic_box, static_box, run
    from pyphysicssandbox import canvas
    from random import randint

    from FS_Tools import make_fs, add_counter_and_make_fs, fallingParagraph
    import drawBot as db

    #=================
    #General Settings:
    #=================
    #👉🏼👉🏼Canvas settings:
    #-------------------
    canvas.shapes = {}
    canvas.window_title = "7H_Texture_GREY_"
    canvas.render_width  = 2000
    canvas.render_height = 1000
    canvas.frames_x_second = 30
    canvas.simulation_render_time = 10
    #Default canvas color:
    canvas.color("Green")

    rw,rh = canvas.render_width, canvas.render_height
    w,h = canvas.win_width, canvas.win_height

    #----------------------
    #Gral physics settings:

    #----------------------
    canvas.gravity(0,400)  ###👈🏼👈🏼GRAVITY:(x,y)
    canvas.resistance(.95) #sandbox default is .95
    gral_elasticity = .9   #sandbox default is .9
    gral_friction   = .6   #sandbox default is .6
    #categories
    cat1 = 0b100
    cat2 = 0b010
    cat3 = 0b001
    #---------------------------------------------------

    ##------------  
    ## Setup data:
    ##------------
    '''
    Setup variables, coordinates, data, etc, here:
    '''
    ##
    ##-------------
    ## World setup:
    ##-------------
    '''
    Setup foor, walls, anchors, etc, here: ---
    '''
    ### World variables:
    floor_h = 200
    floor_color = Color("Red")
    wall_w =  100
    wall_color = Color("Blue")
    y_limit = "floor"

    ###🎨 COLOR SWATCHES: 🎨
    diploe_grey   = rgb_to_normalized(218,219,238,255)
    diploe_yellow = rgb_to_normalized(230,228,102,255)
    diploe_black  = rgb_to_normalized(0,0,0,255)
    ####----------------------------------------

    #### Background
    background = cosmetic_box((0, 0), rw, rh)
    background.color = Color(the_color)
    if the_color == "Grey":
        background.db_color = diploe_grey
    if the_color == "Yellow":
        background.db_color = diploe_yellow

    wall_offset =1500
    left_wall  = static_box((0-wall_offset-wall_w,0), wall_w, rh)
    right_wall = static_box((rw+wall_offset,0), wall_w, rh)

    #### Floor or ceiling: (both use floorH:int)
    if y_limit == "floor":
        floor      = static_box((-rw, rh), rw*4, floor_h)    
    elif y_limit == "ceiling":
        ceiling    = static_box((0, 0-rh), rw, floor_h)

    #floor.color = floor_color
    floor.category = cat1



    #### DrawBot

    ####------------------




    canvas.window_title           = title
    the_fontVariations_A = variations
    
    the_font_path = "fonts/VF/DiploeVF.ttf" 
    the_font_size = 280
    text_color_name = "Black"

    text_box_A = (100, -1000, rw, 1300)
    the_text_A = "Money destroys human roots wherever it is able to penetrate, by turning desire for gain into the sole motive."#"It should draw nourishment from outside contributions only after having digested them"
    the_text_A = "It easily manages to outweigh all other motives because the effort it demands of the mind is so very much less."
    fs_w_counter_A = add_counter_and_make_fs(the_text_A, the_font_path, the_font_size, font_variations=the_fontVariations_A, lineHeight=the_font_size*.8)

    fallingParagraph(fs_w_counter_A, text_box_A, text_color_name,the_font_path, the_font_size, font_variations=the_fontVariations_A,line_angle=(-6,2),category=cat1,split_characters=True)

    run(simulation_on)

#fontVariations_list =[
#                        {"wdth":100,"wght":900,"slnt":0},
#                        {"wdth":150,"wght":900,"slnt":0},
#                        ]


wdth_list = [50]
#wght_list = [200,300,400,500,600,700,900]
wght_list = [300]
slnt_list = [0]

color_list = ["Yellow"]

for the_color in color_list:
    for wght_value in wght_list:
        for wdth_value in wdth_list:
            for slnt_value in slnt_list:
                variations = {"wdth":wdth_value,"wght":wght_value,"slnt":slnt_value}
                title = f"yellow_wdth{wdth_value}_wght{wght_value}_slnt{slnt_value}"
                print(f"💕 {title}")
                makeRender(variations,the_color)

#for variations in fontVariations_list:
#    title = f"{variations}"
#    print(f"💕 {title}")
#    makeRender(variations)