# SQLUser.RBC_WeeklyCycle

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WKC_RowId | bigint | PK |  | NO | - |
| WKC_Code | varchar |  |  | NO | Code |
| WKC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WKC_CreatedDate | date |  |  | SI | Created Date |
| WKC_CreatedTime | time |  |  | SI | Created Time |
| WKC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WKC_Cycle | double |  |  | SI | Cycle |
| WKC_Desc | varchar |  |  | NO | Description |
| WKC_Owner | varchar |  |  | SI | Owner |
| WKC_UpdatedDate | date |  |  | SI | Updated Date |
| WKC_UpdatedTime | time |  |  | SI | Updated Time |
| WKC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*