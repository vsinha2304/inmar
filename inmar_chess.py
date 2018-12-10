import sys
from argparse import ArgumentParser

chess_files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def rook_movement(position):

    files = position[0]
    rank = int(position[1])
    probable_moves = []

    probable_moves.extend([files+str(i) for i in range(1, 9) if i != rank])
    probable_moves.extend([i + str(rank) for i in chess_files if i != files])
    print probable_moves


def knight_movement(position):

    files = position[0]
    rank = int(position[1])

    probable_moves = []

    for i in range(1, 3):

        bef_files = chr(ord(files)-i)
        aft_files = chr(ord(files)+i)

        if bef_files.isalpha() and bef_files in chess_files and i == 1:
            if rank+2 < 8:
                probable_moves.append(bef_files + str(rank + 2))
            if rank-2 > 0:
                probable_moves.append(bef_files + str(rank - 2))

        if bef_files.isalpha() and bef_files in chess_files and i == 2:
            if rank+1 < 8:
                probable_moves.append(bef_files + str(rank + 1))
            if rank-1 > 0:
                probable_moves.append(bef_files + str(rank - 1))

        if aft_files.isalpha() and aft_files in chess_files and i == 1:
            if rank+2 < 8:
                probable_moves.append(aft_files + str(rank + 2))
            if rank-2 > 0:
                probable_moves.append(aft_files + str(rank - 2))

        if aft_files.isalpha() and aft_files in chess_files and i == 2:
            if rank+1 < 8:
                probable_moves.append(aft_files + str(rank + 1))
            if rank-1 > 0:
                probable_moves.append(aft_files + str(rank - 1))

    print probable_moves


def queen_movement(position):
	files = position[0]
    	rank = int(position[1])
    	probable_moves = []

    	probable_moves.extend([files + str(i) for i in range(1, 9) if i != rank])
    	probable_moves.extend([i + str(rank) for i in chess_files if i != files])

	for i in range(1,8):
		if chr(ord(files)+i) in chess_files and rank+i <= 8:
			probable_moves.append(chr(ord(files))+i+str(rank+i))
		elif chr(ord(files)-i) in chess_files and rank-i > 0:
			probable_moves.append(chr(ord(files)+i) + str(rank+i))
		elif chr(ord(files)+i) in chess_files and rank - i > 0:
			probable_moves.append(chr(ord(files)+i) + str(rank - i))
		elif chr(ord(files)-i) in chess_files and rank + i <=8:
			probable_moves.append(chr(ord(files)-i)+ str(rank + i))

        print probable_moves


def main(argv):
        try:
                parser = ArgumentParser()
                parser.add_argument("-piece", dest="piece", help="Chess Piece[Required]")
                parser.add_argument("-position", dest="position", help="Current Position[Required]")

                args = parser.parse_args()

                if args.piece is None:
                    raise Exception("Chess piece name required")

                elif args.position is None:
                    raise Exception("Please provide current piece position")

                chess_piece = str(args.piece)
                current_position = str(args.position)

                if chess_piece.lower() == 'rook':
                	rook_movement(current_position)
                elif chess_piece.lower() == 'knight':
                	knight_movement(current_position)
		elif chess_piece.lower() == 'queen':
			queen_movement(current_position)

        except Exception as ex:
            print "ERROR:%s" % ex.message


if __name__ == '__main__':
    main(sys.argv)
