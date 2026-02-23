# SQLUser.WWW_Translation

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WTRNS_RowID | varchar | PK |  | NO | - |
| WTRNS_Cnt | varchar |  |  | NO | WEB Translation Line Counter |
| WTRNS_Lang | varchar |  |  | NO | WEB Language (see SS_Lang) |
| WTRNS_Page | varchar |  |  | NO | WEB Page reference |
| WTRNS_Text | varchar |  |  | SI | WEB Translated Text |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*