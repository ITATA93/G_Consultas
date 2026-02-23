# SQLUser.SS_MessageRecipient

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MESSREC_RowId | bigint | PK |  | NO | - |
| MESSREC_DateRead | date |  |  | SI | Date Read |
| MESSREC_Message_DR | bigint |  | FK | SI | Des Ref Message |
| MESSREC_TimeRead | time |  |  | SI | Time Read |
| MESSREC_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*