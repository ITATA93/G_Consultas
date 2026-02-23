# web_Msg_Pharmacy.PrescEdit

**Schema:** web_Msg_Pharmacy
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| BatchID | varchar |  |  | SI | - |
| BatchPick | varchar |  |  | SI | - |
| BatchTaken | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| OrdItemID | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| RegNoIDs | varchar |  |  | SI | - |
| RegNoTaken | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*