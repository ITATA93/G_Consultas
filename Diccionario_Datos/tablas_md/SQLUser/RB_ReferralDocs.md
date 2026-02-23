# SQLUser.RB_ReferralDocs

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOC_ParRef | bigint | PK |  | NO | RB_Referral Parent Reference |
| DOC_Childsub | double |  |  | NO | Childsub |
| DOC_DateCreated | date |  |  | SI | DateCreated |
| DOC_Desc | varchar |  |  | SI | Description |
| DOC_Doc_DR | bigint |  | FK | SI | Des Ref Doc |
| DOC_Path | varchar |  |  | SI | Path |
| DOC_RowId | varchar |  |  | NO | - |
| DOC_TimeCreated | time |  |  | SI | TimeCreated |
| DOC_Type | varchar |  |  | SI | Type |
| DOC_UserCreated_DR | bigint |  | FK | SI | Des Ref UserCreated |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*