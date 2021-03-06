# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 01:33:37 by hkono             #+#    #+#              #
#    Updated: 2021/04/22 12:16:11 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Robot import roboter
from Robot.System import Chat


def main():
    Robo = Chat.ToHuman()
    roboter.StartUp(Robo)


if __name__ == '__main__':
    main()
