# SQLUser.RB_ReferralStatusHistory

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STH_ParRef | bigint | PK |  | NO | RB_Referral Parent Reference |
| STH_Childsub | double |  |  | NO | Childsub |
| STH_Comments | varchar |  |  | SI | comments |
| STH_DateCreated | date |  |  | SI | DateCreated |
| STH_ReasonForChange | varchar |  |  | SI | Description |
| STH_RowId | varchar |  |  | NO | - |
| STH_Status | varchar |  |  | SI | Type |
| STH_TimeCreated | time |  |  | SI | TimeCreated |
| STH_UserCreated_DR | bigint |  | FK | SI | Des Ref UserCreated |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*