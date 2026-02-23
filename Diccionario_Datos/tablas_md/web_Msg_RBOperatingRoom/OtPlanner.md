# web_Msg_RBOperatingRoom.OtPlanner

**Schema:** web_Msg_RBOperatingRoom
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico (Web)**. Interfaz de gestión de cirugías y programación de pabellones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| RBOperRoomID | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SchedID | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*