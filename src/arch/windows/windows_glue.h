/*
Cubesat Space Protocol - A small network-layer protocol designed for Cubesats
Copyright (C) 2012 Gomspace ApS (http://www.gomspace.com)
Copyright (C) 2012 AAUSAT3 Project (http://aausat3.space.aau.dk) 

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
*/

#ifndef WINDOWS_GLUE_H
#define WINDOWS_GLUE_H

#include <Windows.h>
#undef interface

#if (_WIN32_WINNT >= 0x0600)
#ifndef RTL_CONDITION_VARIABLE_INIT

#define RTL_CONDITION_VARIABLE_INIT 0
#define RTL_CONDITION_VARIABLE_LOCKMODE_SHARED 1
#define CONDITION_VARIABLE_INIT RTL_CONDITION_VARIABLE_INIT
#define CONDITION_VARIABLE_LOCKMODE_SHARED RTL_CONDITION_VARIABLE_LOCKMODE_SHARED

typedef PVOID RTL_CONDITION_VARIABLE;
typedef RTL_CONDITION_VARIABLE CONDITION_VARIABLE, *PCONDITION_VARIABLE;

WINBASEAPI VOID WINAPI InitializeConditionVariable(PCONDITION_VARIABLE ConditionVariable);
WINBASEAPI WINBOOL WINAPI SleepConditionVariableCS(PCONDITION_VARIABLE ConditionVariable, PCRITICAL_SECTION CriticalSection, DWORD dwMilliseconds);
WINBASEAPI VOID WINAPI WakeAllConditionVariable(PCONDITION_VARIABLE ConditionVariable);
WINBASEAPI VOID WINAPI WakeConditionVariable(PCONDITION_VARIABLE ConditionVariable);

#endif // RTL_CONDITION_VARIABLE_INIT
#endif // _WIN32_WINNT
#endif
