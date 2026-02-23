# SQLUser.SS_Message

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MESS_RowId | bigint | PK |  | NO | - |
| MESS_DateCreated | date |  |  | SI | Date Created |
| MESS_EncodeHTMLLink | bit |  |  | SI | Flag to manage if message entered by User in compo... |
| MESS_Link | varchar |  |  | SI | Message |
| MESS_Message | varchar |  |  | SI | Message |
| MESS_TimeCreated | time |  |  | SI | Time Created |
| MESS_Urgent | varchar |  |  | SI | Urgent |
| MESS_UserCreated_DR | bigint |  | FK | SI | Des Ref UserCreated |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*